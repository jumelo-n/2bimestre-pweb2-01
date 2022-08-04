import datetime
from django import forms


class SignoForm(forms.Form):
    day = forms.DateField(input_formats=['%d/%m/%Y'])
    time = forms.TimeField()
