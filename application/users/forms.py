from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Visitor

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    class Meta:
        model = Visitor
        fields = ('login', 'password', 'name')

class AuthorizationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    class Meta:
        model = Visitor
        fields = ('login', 'password')


# формы