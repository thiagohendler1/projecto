from django import forms
from .models import *

class ComprarFormulario(forms.ModelForm):
    class Meta:
        model = Libro_buy
        fields = '__all__'
        

class VenderFormulario(forms.ModelForm):
    class Meta:
        model = Libro_sell
        fields = '__all__'

class LeidosFormulario(forms.ModelForm):
    class Meta:
        model = Libro_leído
        fields = '__all__'