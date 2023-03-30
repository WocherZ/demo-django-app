from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .forms import ReleForm
from users.models import Visitor
from .models import *
from .schemas_draw import visualizaton
from .mqtt_sender import MqttWorker
import time
import math

# Главная страница
class HomeView(View):
    def get(self, request):
        context = {}

        return render(request, 'app/home.html', context)

class AboutView(View):
    def get(self, request):
        context = {}
        return render(request, 'app/about.html', context)


# ЛИЧНЫЙ КАБИНЕТ
class PersonalPage(View):
    def get(self, request):
        context = {}

        # для VISITOR
        if request.session['user_group'] == 'VISITOR':
            login = request.session['login']
            visitor = Visitor.objects.all().get(login=login)
            context['visitor'] = visitor
            context['current_price'] = visitor.tariff * visitor.consumed_energy

        # для ADMIN
        if request.session['user_group'] == 'ADMIN':
            context['users'] = Visitor.objects.all()

        if request.session['user_group'] == 'OPERATOR':
            pass

        return render(request, 'app/personal_page.html', context)

# Выход пользователя - сброс сессии
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
                   'sensor_id': visitor.sensor_id.sensor_id,
                   }
        return render(request, 'app/info_page.html', context=context)


# Принятие данных с датчиков из gateway
class getTemperature(View):
    def post(self, request):
        sensor_id = int(request.POST['sensor_id'])
        temperature = float(request.POST['temperature'])
        humanity = float(request.POST['humanity'])
        print(humanity)
        if sensor_id < 16 and not math.isnan(temperature) and not math.isnan(humanity):
            print("Данные с датчиков:", sensor_id, temperature, humanity)
            TemperatureHistory.create_record(sensor_id, temperature, humanity)
            return HttpResponse("OK")
        else:
            return HttpResponse("404")

# ФОРМА ОПЕРАТОРА
class OperatorFormView(View):
    def get(self, request):
        context = {}
        context['form'] = ReleForm()
        return render(request, 'app/operator_form.html', context)

    # Форма с реле
    def post(self, request):
        if (RelayCondition.objects.all() == None):
            RelayCondition.create_relays()

        # Принитие данных и запись в БД
        values_checkbox = {}
        for i in range(1, MAX_NUMBER_RELAY+1):
            if request.POST.get('checkbox' + str(i)) != None:
                values_checkbox[i-1] = request.POST['checkbox' + str(i)]
        RelayCondition.write_values(values_checkbox)

        # MQTT отправка состояний реле
        mqtt_sender = MqttWorker()
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition.objects.get(relay_id=i)
            relay_state = 1 if relay.condition else 0
            print(relay.relay_id, relay_state)
            mqtt_sender.send_state_2bytes(relay.relay_id, relay_state)
        mqtt_sender.disconnect()

        # Сохранение картинки svg - схемы
        reles = [0]*(max(values_checkbox.keys() if values_checkbox.keys() else [0])+1)
        for box in values_checkbox.keys():
            reles[box] = 1 if values_checkbox[box] == 'on' else 0
        visualizer = visualizaton()
        if len(reles) > 30:
            visualizer.plot_single_bloc(*reles[:30])
        else:
            visualizer.plot_single_bloc(*reles)
        time.sleep(2)

        context = {}
        context['form'] = ReleForm(request.POST)
        return render(request, 'app/operator_form.html', context)


class ConsumerSourceView(View):
    def get(self, request):
        context = {}
        context['users'] = Visitor.objects.all()
        return render(request, 'app/consumer_source.html', context)


def power_supply_view(request):
    return render(request, 'app/power_supply.html')


