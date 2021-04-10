#from home.models import Barbero
from django import forms
from django.forms import fields, widgets
from.models import *


class contacto_form (forms.Form):

    Correo= forms.EmailField(widget= forms.TextInput())
    asunto = forms.CharField(widget= forms.TextInput())
    texto = forms.CharField(widget= forms.Textarea())

class agregar_barbero_form(forms.ModelForm):
    class Meta:
        model = Barbero
        fields = '__all__'
        fields = ['nombre','apellido', 'alias', 'foto']


class agregar_servicio_form(forms.ModelForm):
     class Meta:
         model = Servicio
         fields = '__all__'
         fields = ['nombre','descripcion','precio']


         