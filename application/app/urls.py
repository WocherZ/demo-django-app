from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('personal_page/<int:id>', views.PersonalPage.as_view(), name=personal_page)
]