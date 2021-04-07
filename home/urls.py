from django.urls import path
from .views import *



urlpatterns = [


path('equipo/',vista_equipo),
path('',vista_inicio),
path('servicio/',vista_servicio),
path('productos/',vista_productos),
path('contacto/',vista_contacto),
path('registro/',vista_registro),
path('inicio_sesion/',vista_inicio_sesion),
path('solicitar_cita/',vista_solicitar_cita),


#path('agregar_barbero/',vista_agregar_barbero,name='agregar_barbero')

]


