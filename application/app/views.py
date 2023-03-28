from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
def add_role_context():
    pass

class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html', {'role': 'Andrew'})

class AboutView(View):
    def get(self, request):
        return render(request, 'app/about.html')


class PersonalPage(View):
    def get(self, request):
        print(request.user)
        print(request.user.group)
        # TODO отображение индивидуальной инфы
        return render(request, 'app/personal_page.html')

def logout(request):
    # del request.session['role']
    # del request.session['user_id']
    # request.session['is_login'] = False
    return redirect('home')


