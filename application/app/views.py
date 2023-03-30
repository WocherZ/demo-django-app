from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .forms import ReleForm
from users.models import Visitor
from .models import *
from .schemas_draw import visualizaton
from .mqtt_sender import MqttWorker
import time

class HomeView(View):
    def get(self, request):
        context = {}

        return render(request, 'app/home.html', context)

class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, 'app/about.html', context)


class PersonalPage(View):
    def get(self, request):
        context = {}
        # TODO отображение индивидуальной инфы
        if request.session['user_group'] == 'ADMIN':
            context['users'] = Visitor.objects.all()
        return render(request, 'app/personal_page.html', context)

def logout(request):
    request.session['login'] = None
    request.session['user_group'] = None
    return redirect('home')

# Только для админов(просмотр пользователей)
class InfoPage(View):
    def get(self, request, id):
        visitor = get_object_or_404(Visitor, pk=id)
        print(visitor)
        context = {'visitor': visitor,
                   'current_price': visitor.tariff * visitor.consumed_energy,
                   'sensor_id': TemperatureSensor.get_sensor_by_visitor_id(id).sensor_id}
        return render(request, 'app/info_page.html', context=context)

class getTemperature(View):
    def post(self, request):
        sensor_id = int(request.POST['sensor_id'])
        temperature = float(request.POST['temperature'])
        humanity = float(request.POST['humanity'])
        if sensor_id < 16:
            print("Данные с датчиков:", sensor_id, temperature, humanity)
            TemperatureHistory.create_record(sensor_id, temperature, humanity)
            return HttpResponse("OK")
        else:
            return HttpResponse("404")

class OperatorFormView(View):
    def get(self, request):
        context = {}
        context['form'] = ReleForm()
        return render(request, 'app/operator_form.html', context)

    def post(self, request):
        if (RelayCondition.objects.all() == None):
            RelayCondition.create_relays()

        values_checkbox = {}
        print(request.POST)
        for i in range(1, MAX_NUMBER_RELAY+1):
            if request.POST.get('checkbox' + str(i)) != None:
                values_checkbox[i-1] = request.POST['checkbox' + str(i)]
                print(request.POST['checkbox' + str(i)])
        print(values_checkbox)

        RelayCondition.write_values(values_checkbox)

        reles = [0]*(max(values_checkbox.keys() if values_checkbox.keys() else [0])+1)
        for box in values_checkbox.keys():
            reles[box] = 1 if values_checkbox[box] == 'on' else 0
        visualizer = visualizaton()
        if len(reles) > 30:
            visualizer.plot_single_bloc(*reles[:30])
        else:
            visualizer.plot_single_bloc(*reles)
        time.sleep(1)

        # TODO - MQTT SEND
        mqtt_sender = MqttWorker()
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition.objects.get(relay_id=i)
            relay_state = 1 if relay.condition else 0
            print(relay.relay_id, relay_state)
            mqtt_sender.send_state_2bytes(relay.relay_id, relay_state)

        mqtt_sender.disconnect()

        context = {}
        context['form'] = ReleForm()
        return render(request, 'app/operator_form.html', context)


class ConsumerSourceView(View):
    def get(self, request):
        context = {}
        context['users'] = Visitor.objects.all()
        return render(request, 'app/consumer_source.html', context)

def power_supply_view(request):
    return render(request, 'app/power_supply.html')


