from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Visitor

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    class Meta:
        model = Visitor
        fields = ('login', 'password')