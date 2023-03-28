from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

from .forms import ReleForm

def add_role_context(request, context):
    # if request.user is AnonymousUser:
    #
    #     return
    if user_group is None:
        context['role'] = user_group
    else:
        context['role'] = None


class HomeView(View):
    def get(self, request):
        context = {}
        add_role_context(request, context)
        return render(request, 'app/home.html', context)

class AboutView(View):
    def get(self, request):
        context = {}
        add_role_context(request, context)
        return render(request, 'app/about.html', context)


class PersonalPage(View):
    def get(self, request):
        context = {}
        context['form'] = ReleForm()
        add_role_context(request, context)
        #print(request.user)
        #print(request.user.group)
        # TODO отображение индивидуальной инфы
        return render(request, 'app/personal_page.html', context)

def logout(request):
    request.user = None
    return redirect('home')


