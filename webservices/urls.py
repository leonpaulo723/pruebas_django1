from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'producto', producto_viewset)
router.register(r'persona', persona_viewset)
router.register(r'barbero', barbero_viewset)
router.register(r'servicio', servicio_viewset)
router.register(r'cita', cita_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

    
]

