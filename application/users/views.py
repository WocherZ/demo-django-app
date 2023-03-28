import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views import View

from .forms import RegistrationForm, AuthorizationForm

class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        return success_url

class AuthorizationView(View):
    def get(self, request):
        context = {'form': AuthorizationForm()}
        return render(request, 'users/login.html', context=context)

    def post(self, request):
        print(request.POST)
        # TODO - СВЕРКА ПОЛЬЗОВАТЕЛЯ
        context = {'form': AuthorizationForm()}
        return redirect('home')
        #return render(request, 'users/login.html', context=context)

