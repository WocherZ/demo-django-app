import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.views import View

from .forms import RegistrationForm, AuthorizationForm
from .models import Visitor


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
        context = {}

        print('Login: ' + str(request.session.get('login')))
        context = {'form': AuthorizationForm()}
        return render(request, 'users/login.html', context=context)

    def post(self, request):
        context = {'form': AuthorizationForm()}

        login = request.POST['login']
        password = request.POST['password']
        if Visitor.objects.filter(login = login).first():
            user = Visitor.objects.filter(login = login).first()
            if password == user.password:
                request.session['login'] = login
                request.session['user_group'] = user.group
                return redirect('home')
            else:
                context['error'] = 'Неверный логин или пароль!'


        return render(request, 'users/login.html', context=context)

