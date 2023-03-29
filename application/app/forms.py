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
    checkbox7 = forms.BooleanField(label='Реле 7', required=False)
    textbox7 = forms.IntegerField(label='Число 7', initial=0, min_value=0, max_value=100)
    checkbox8 = forms.BooleanField(label='Реле 8', required=False)
    textbox8 = forms.IntegerField(label='Число 8', initial=0, min_value=0, max_value=100)
    checkbox9 = forms.BooleanField(label='Реле 9', required=False)
    textbox9 = forms.IntegerField(label='Число 9', initial=0, min_value=0, max_value=100)
    сheckbox10 = forms.BooleanField(label='Реле 10', required=False)
    textbox10 = forms.IntegerField(label='Число 10', initial=0, min_value=0, max_value=100)
    checkbox11 = forms.BooleanField(label='Реле 11', required=False)
    textbox11 = forms.IntegerField(label='Число 11', initial=0, min_value=0, max_value=100)
    checkbox12 = forms.BooleanField(label='Реле 12', required=False)
    textbox12 = forms.IntegerField(label='Число 12', initial=0, min_value=0, max_value=100)
    checkbox13 = forms.BooleanField(label='Реле 13', required=False)
    textbox13 = forms.IntegerField(label='Число 13', initial=0, min_value=0, max_value=100)
    checkbox14 = forms.BooleanField(label='Реле 14', required=False)
    textbox14 = forms.IntegerField(label='Число 14', initial=0, min_value=0, max_value=100)
    checkbox15 = forms.BooleanField(label='Реле 15', required=False)
    textbox15 = forms.IntegerField(label='Число 15', initial=0, min_value=0, max_value=100)
    heckbox16 = forms.BooleanField(label='Реле 16', required=False)
    textbox16 = forms.IntegerField(label='Число 16', initial=0, min_value=0, max_value=100)
    checkbox17 = forms.BooleanField(label='Реле 17', required=False)
    textbox17 = forms.IntegerField(label='Число 17', initial=0, min_value=0, max_value=100)
    checkbox18 = forms.BooleanField(label='Реле 18', required=False)
    textbox18 = forms.IntegerField(label='Число 18', initial=0, min_value=0, max_value=100)
    checkbox19 = forms.BooleanField(label='Реле 19', required=False)
    textbox19 = forms.IntegerField(label='Число 19', initial=0, min_value=0, max_value=100)
    checkbox20 = forms.BooleanField(label='Реле 20', required=False)
    textbox20 = forms.IntegerField(label='Число 20', initial=0, min_value=0, max_value=100)
    checkbox21 = forms.BooleanField(label='Реле 21', required=False)
    textbox21 = forms.IntegerField(label='Число 21', initial=0, min_value=0, max_value=100)
    сheckbox22 = forms.BooleanField(label='Реле 22', required=False)
    textbox22 = forms.IntegerField(label='Число 22', initial=0, min_value=0, max_value=100)
    checkbox23 = forms.BooleanField(label='Реле 23', required=False)
    textbox23 = forms.IntegerField(label='Число 23', initial=0, min_value=0, max_value=100)
    checkbox24 = forms.BooleanField(label='Реле 24', required=False)
    textbox24 = forms.IntegerField(label='Число 24', initial=0, min_value=0, max_value=100)
    checkbox25 = forms.BooleanField(label='Реле 25', required=False)
    textbox25 = forms.IntegerField(label='Число 25', initial=0, min_value=0, max_value=100)
    checkbox26 = forms.BooleanField(label='Реле 26', required=False)
    textbox26 = forms.IntegerField(label='Число 26', initial=0, min_value=0, max_value=100)
    checkbox27 = forms.BooleanField(label='Реле 27', required=False)
    textbox27 = forms.IntegerField(label='Число 27', initial=0, min_value=0, max_value=100)
    heckbox28 = forms.BooleanField(label='Реле 28', required=False)
    textbox28 = forms.IntegerField(label='Число 28', initial=0, min_value=0, max_value=100)
    checkbox29 = forms.BooleanField(label='Реле 29', required=False)
    textbox29 = forms.IntegerField(label='Число 29', initial=0, min_value=0, max_value=100)
    checkbox30 = forms.BooleanField(label='Реле 30', required=False)
    textbox30 = forms.IntegerField(label='Число 30', initial=0, min_value=0, max_value=100)
    checkbox31 = forms.BooleanField(label='Реле 31', required=False)
    # textbox31 = forms.IntegerField(label='Число 31', initial=0, min_value=0, max_value=100)
    checkbox32 = forms.BooleanField(label='Реле 32', required=False)
    # textbox32 = forms.IntegerField(label='Число 32', initial=0, min_value=0, max_value=100)
    checkbox33 = forms.BooleanField(label='Реле 33', required=False)
    # textbox33 = forms.IntegerField(label='Число 33', initial=0, min_value=0, max_value=100)
    сheckbox34 = forms.BooleanField(label='Реле 34', required=False)
    # textbox34 = forms.IntegerField(label='Число 34', initial=0, min_value=0, max_value=100)
    checkbox35 = forms.BooleanField(label='Реле 35', required=False)
    # textbox35 = forms.IntegerField(label='Число 35', initial=0, min_value=0, max_value=100)
    checkbox36 = forms.BooleanField(label='Реле 36', required=False)
    # textbox36 = forms.IntegerField(label='Число 36', initial=0, min_value=0, max_value=100)
