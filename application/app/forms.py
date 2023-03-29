from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ReleForm(forms.Form):
    checkbox1 = forms.BooleanField(label='Реле 1', required=False)
    textbox1 = forms.IntegerField(label='Число 1', initial=0, min_value=0, max_value=100)
    checkbox2 = forms.BooleanField(label='Реле 2', required=False)
    textbox2 = forms.IntegerField(label='Число 2', initial=0, min_value=0, max_value=100)
    checkbox3 = forms.BooleanField(label='Реле 3', required=False)
    textbox3 = forms.IntegerField(label='Число 3', initial=0, min_value=0, max_value=100)
    heckbox4 = forms.BooleanField(label='Реле 4', required=False)
    textbox4 = forms.IntegerField(label='Число 4', initial=0, min_value=0, max_value=100)
    checkbox5 = forms.BooleanField(label='Реле 5', required=False)
    textbox5 = forms.IntegerField(label='Число 5', initial=0, min_value=0, max_value=100)
    checkbox6 = forms.BooleanField(label='Реле 6', required=False)
    textbox6 = forms.IntegerField(label='Число 6', initial=0, min_value=0, max_value=100)


# формы