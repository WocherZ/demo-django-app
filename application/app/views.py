from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .forms import ReleForm
from users.models import Visitor



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

def logout(request):
    request.session['login'] = None
    request.session['user_group'] = None
    return redirect('home')


def info_view(request):
    return render(request, 'app/info_page.html')

