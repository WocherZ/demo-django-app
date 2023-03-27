from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView


from .forms import RegistrationForm

class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm