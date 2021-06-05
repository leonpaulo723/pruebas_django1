from django.urls import path
from .views import *




urlpatterns = [



path('',vista_inicio),
#path('servicio/',vista_servicio),

path('contacto/',vista_contacto),

path('inicio_sesion/',vista_inicio_sesion),

path('nosotros/',vista_nosotros),


#barbero
path('listar_barbero/',listar_barbero, name='listar_barbero'),
path('agregar_barbero/',agregar_barbero, name='agregar_barbero'),
path('editar_barbero/<int:id_br>/',editar_barbero, name='editar_barbero'),
path('eliminar_barbero/<int:id_br>/',eliminar_barbero, name='eliminar_barbero'),

path('ver_barbero/',ver_barbero, name='ver_barbero'),


#servicio
path('listar_servicio/',listar_servicio, name='listar_servicio'),
path('agregar_servicio/',agregar_servicio, name='agregar_servicio'),
path('editar_servicio/<int:id_br>/',editar_servicio, name='editar_servicio'),
path('eliminar_servicio/<int:id_br>/',eliminar_servicio, name='eliminar_servicio'),



#CLIENTE
path('crear_cita/',agendar_cita, name='crear_cita'),



]


