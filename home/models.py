from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500)
    marca = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to = 'productos', null=True, blank=True )
    
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=400)
    telefono = models.IntegerField()
    foto = models.ImageField(upload_to = 'clientes', null=True, blank=True)
    user = models.OneToOneField(User, on_delete = models.PROTECT,default=True)

    def __str__(self):
        return str(self.cedula)

class Barbero(models.Model):
    nombre = models.CharField(max_length=400)
    descripcion = models.TextField(max_length=5000)
    foto = models.ImageField(upload_to = 'barberos', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=400)
    descripcion = models.TextField(max_length=5000)
    tiempo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    icono = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to = 'servicios', null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Cita(models.Model):
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha = models.DateField()
    hora = models.TimeField()
    jornada = models.CharField(max_length=120)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    barbero = models.ForeignKey(Barbero, on_delete=models.PROTECT)
    servicios = models.ManyToManyField(Servicio, blank=True)
    

    def __str__(self):
        return str(self.fecha_creacion)