from rest_framework import serializers
from home.models import *




class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'nombre', 'descripcion', 'marca', 'precio', 'estado', 'foto')

class persona_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('url', 'cedula', 'correo', 'telefono', 'foto')

class barbero_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barbero
        fields = ('url', 'nombre', 'descripcion', 'foto')

class servicio_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = ('url', 'nombre', 'descripcion', 'tiempo', 'precio', 'icono', 'foto')

class cita_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cita
        fields = ('url', 'fecha', 'hora','persona', 'barbero', 'servicios')
