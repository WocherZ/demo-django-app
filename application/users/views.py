from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView


from .forms import RegistrationForm

# class RegistrationView(CreateView):
#     template_name = 'users/register.html'
#     form_class = RegistrationForm

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def home(request):
    return render(request, 'app/home.html')