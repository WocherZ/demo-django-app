import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView


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

class AuthorizationView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthorizationForm
    redirect_authenticated_user = True
    # def get(self, request, *args, **kwargs):
    #     context = {'form': AuthorizationForm()}
    #     return render(request, 'users/login.html', context=context)

    def get_success_url(self):
        print("Залогинился пользователь!")

        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
