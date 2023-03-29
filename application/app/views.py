from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .forms import ReleForm
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
        return render(request, 'app/personal_page.html', context)

def logout(request):
    request.session['login'] = None
    request.session['user_group'] = None
    return redirect('home')


class getTemperature(View):
    def post(self, request):
        TemperatureHistory.delete_all_records()
        print("Пришла температура")
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


