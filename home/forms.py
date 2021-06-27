#from home.models import Barbero
from django import forms
from django.forms import fields, widgets

from.models import *





class agregar_barbero_form(forms.ModelForm):
    class Meta:
        model = Barbero
        fields = '__all__'
        


class agregar_servicio_form(forms.ModelForm):
     class Meta:
         model = Servicio
         fields = '__all__'
         #fields = ['nombre','descripcion','precio']


class agregar_cita_form(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        exclude = ['persona']
        #fields = ['fecha','hora','jornada']


class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())
    clave = forms.CharField(widget=forms.PasswordInput(render_value=False))


class user_form (forms.ModelForm):
    password = forms.CharField(label='clave', widget=forms.PasswordInput(render_value=False))
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'password','email']

class registrate_form (forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ['user','correo']


class crear_prod_form (forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ['estado']
    


        





