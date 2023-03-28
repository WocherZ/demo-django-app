from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')


class PersonalPage(View):
    def get(self, request, id):
        # TODO отображение индивидуальной инфы
        return render(request, 'app/personal_page.html')

def logout(request):
    del request.session['role']
    del request.session['user_id']
    request.session['is_login'] = False
    return redirect('home')


