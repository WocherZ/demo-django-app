from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView


from .forms import RegistrationForm, AuthorizationForm

class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm

class AuthorizationView(CreateView):
    template_name = 'users/login.html'
    form_class = AuthorizationForm

def login(request):
    return render(request, 'users/login.html')

def home(request):
    return render(request, 'app/home.html', {'role': 'Andrew'})