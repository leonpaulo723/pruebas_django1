from django.urls import path
from .views import *




urlpatterns = [



path('',vista_inicio, name='inicio'),
path('servicios/', vista_servicios, name = 'servicios'),
path( 'index/', vista_index),


#login
path('login/',vista_login, name='vista_login'),
path('logout/',vista_logout, name='vista_logout'),
path('registrate/', vista_registrate),

path('agenda/', vista_agenda),

#barbero
path('equipo/',listar_barbero, name='listar_barbero'),
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

#PRODUCTO
path('crear_producto/',crear_producto,name='crear_producto')




]


