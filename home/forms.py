from django import forms
from django.forms import widgets


class contacto_form (forms.Form):

    Correo= forms.EmailField(widget= forms.TextInput())
    asunto = forms.CharField(widget= forms.TextInput())
    texto = forms.CharField(widget= forms.Textarea())
 