from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .forms import ReleForm
from users.models import Visitor
from .models import *



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
        context['form'] = ReleForm()
        # TODO отображение индивидуальной инфы
        if request.session['user_group'] == 'ADMIN':
            context['users'] = Visitor.objects.all()
        return render(request, 'app/personal_page.html', context)

    def post(self, request):
        if (RelayCondition.objects.all() == None):
            RelayCondition.create_relays()

        values_checkbox = {}
        print(request.POST)
        for i in range(1, MAX_NUMBER_RELAY+1):
            if request.POST.get('checkbox' + str(i)) != None:
                values_checkbox[i] = request.POST['checkbox' + str(i)]
                print(request.POST['checkbox' + str(i)])
        print(values_checkbox)
        RelayCondition.write_values(values_checkbox)

        return redirect('personal_page')

def logout(request):
    request.session['login'] = None
    request.session['user_group'] = None
    return redirect('home')


def info_view(request):
    return render(request, 'app/info_page.html')

class getTemperature(View):
    def post(self, request):
        print(request.POST['sensor_id'], type(request.POST['sensor_id']))
        print(request.POST['temperature'], type(request.POST['temperature']))
        print(request.POST['humanity'], type(request.POST['humanity']))
        sensor_id = int(request.POST['sensor_id'])
        temperature = float(request.POST['temperature'])
        humanity = float(request.POST['humanity'])
        if sensor_id < 16:
            TemperatureHistory.create_record(sensor_id, temperature, humanity)
            return HttpResponse("OK")
        else:
            return HttpResponse("404")


