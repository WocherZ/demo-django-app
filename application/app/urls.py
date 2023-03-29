from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('personal_page', views.PersonalPage.as_view(), name='personal_page'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('info_page/<int:id>', views.InfoPage.as_view(), name='info_page'),
    path('get_temperature/', views.getTemperature.as_view(), name='get_temperature'),
]