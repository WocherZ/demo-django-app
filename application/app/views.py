from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

# from .forms import ReleForm
from users.models import Visitor
from .models import *
from .schemas_draw import visualizaton
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

            sensor_id = visitor.sensor_id.sensor_id
            print(sensor_id)
            temp = TemperatureHistory.objects.all().filter(sensor=sensor_id)[0].temperature
            hum = TemperatureHistory.objects.all().filter(sensor=sensor_id).order_by('-id')[0].humanity
            # TODO change filter
            context['curr_temperature'] = temp
            context['curr_humidity'] = hum

            context['temp_history'] = [obj.temperature for obj in TemperatureHistory.objects.filter(sensor=sensor_id)]
            context['hum_history'] = [obj.humanity for obj in TemperatureHistory.objects.filter(sensor=sensor_id)]

        if request.session['user_group'] == 'VISITOR_2FLOOR':
            login = request.session['login']
            visitor = Visitor.objects.all().get(login=login)
            context['visitor'] = visitor
            context['current_price'] = visitor.tariff * visitor.consumed_energy

            sensor_id = visitor.sensor_id.sensor_id
            temp = TemperatureHistory.objects.all().filter(sensor=sensor_id)[0].temperature
            hum = TemperatureHistory.objects.all().filter(sensor=sensor_id)[0].humanity
            context['curr_temperature'] = temp
            context['curr_humidity'] = hum

        # для ADMIN
        if request.session['user_group'] == 'ADMIN':
            context['users'] = Visitor.objects.all()

        return render(request, 'app/personal_page.html', context)

# Выход пользователя - сброс сессии
# def logout(request):
#     request.session['login'] = None
#     request.session['user_group'] = None
#     return redirect('home')


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

def off_relay_if_limit_temp(sensor_id, current_temp, limit_value, relay_id):
    if sensor_id == 1:
        if current_temp >= limit_value:
            mqtt_sender = MqttWorker()
            mqtt_sender.send_state_2bytes(relay_id, 0)
            mqtt_sender.disconnect()
            print("Послан сигнал на выключение реле:", relay_id)
            return True
    return False


CRITICAL_RELAYS = 15
SENSOR = 4
# Принятие данных с датчиков из gateway
class getTemperature(View):
    def post(self, request):
        sensor_id = int(request.POST['sensor_id'])
        temperature = float(request.POST['temperature'])
        humanity = float(request.POST['humanity'])
        if (sensor_id < 16) and (not math.isnan(temperature)) and (not math.isnan(humanity)):

            if sensor_id == SENSOR:
                if temperature >= 27.0:
                    mqtt_sender = MqttWorker()
                    mqtt_sender.send_state_2bytes(CRITICAL_RELAYS, 0)
                    mqtt_sender.disconnect()
                    print("Послан сигнал на выключение реле:", CRITICAL_RELAYS)

                else:
                    mqtt_sender = MqttWorker()
                    mqtt_sender.send_state_2bytes(CRITICAL_RELAYS, 1)
                    mqtt_sender.disconnect()
                    print("Послан сигнал на включение реле:", CRITICAL_RELAYS)



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
        # mqtt_sender = MqttWorker()
        context = {}
        context['form'] = ReleForm(request.POST)

        # mqtt_sender = MqttWorker()
        for i in range(MAX_NUMBER_RELAY):
            relay = RelayCondition.objects.get(relay_id=i)
            relay_state = 1 if relay.condition else 0
            print(relay.relay_id, relay_state)
        #     mqtt_sender.send_state_2bytes(relay.relay_id, relay_state)
        # mqtt_sender.disconnect()

        # Сохранение картинки svg - схемы
        reles = [0]*(max(values_checkbox.keys() if values_checkbox.keys() else [0])+1)
        for box in values_checkbox.keys():
            reles[box] = 1 if values_checkbox[box] == 'on' else 0
        visualizer = visualizaton()

        added_zeros = (36 - len(reles))*[0]
        visualizer.plot_scheme(*reles, *added_zeros)
        time.sleep(2)

        return render(request, 'app/operator_form.html', context)


class ConsumerSourceView(View):
    def get(self, request):
        context = {}
        context['user_id'] = []
        context['sourse_id'] = []
        i = 0
        for user in Visitor.objects.all():
            context['sourse_id'].append((user.id // 8 + 1, user.id))
            context['user_id'].append(user.id)
        context['everything'] = context['user_id'] + context['sourse_id']
        return render(request, 'app/consumer_source.html', context=context)


def power_supply_view(request):
    context = {}
    N = RelayCondition.objects.all().filter(condition=True).all().count()
    first = int(RelayCondition.objects.all().get(relay_id = 1).condition)
    context['power'] = round((N-first)*0.8, 1)
    context['KPD'] = round(100 * 0.5 / (0.5 + 0.12))
    return render(request, 'app/power_supply.html', context)


