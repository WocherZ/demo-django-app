from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')
