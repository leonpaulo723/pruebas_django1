from django.urls import path
from .views import *



urlpatterns = [



path('',vista_inicio),
path('servicio/',vista_servicio),

path('contacto/',vista_contacto),

path('inicio_sesion/',vista_inicio_sesion),


#barbero
path('listar_barbero/',listar_barbero, name='listar_barbero'),
path('agregar_barbero/',agregar_barbero, name='agregar_barbero'),
path('editar_barbero/<int:id_br>/',editar_barbero, name='editar_barbero'),
path('eliminar_barbero/',eliminar_barbero, name='eliminar_barbero'),

path('ver_barbero/',ver_barbero, name='ver_barbero'),


#servicio
path('listar_servicios/',listar_servicios, name='listar_servicios'),
path('agregar_servicios/',agregar_servicios, name='agregar_servicios'),


]


