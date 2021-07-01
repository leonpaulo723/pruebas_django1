from home.models import *
from .serializer import *
from rest_framework import viewsets



# Create your views here.

class producto_viewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = producto_serializer

class persona_viewset(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = persona_serializer

class barbero_viewset(viewsets.ModelViewSet):
    queryset = Barbero.objects.all()
    serializers_class = barbero_serializer

class servicio_viewset(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = servicio_serializer
    
class cita_viewset(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = cita_serializer





