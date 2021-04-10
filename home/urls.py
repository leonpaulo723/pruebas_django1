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

#barbero
path('listar_barbero/',listar_barbero, name='listar_barbero'),
path('agregar_barbero/',agregar_barbero, name='agregar_barbero'),
path('editar_barbero/<int:id_br>/',editar_barbero, name='editar_barbero'),
path('eliminar_barbero/',eliminar_barbero, name='eliminar_barbero'),

#servicio



]


