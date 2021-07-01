from django.db import models
from django.contrib.auth.models import User

#tupla
horarios = (
    ("8:00 - 9:00", "8:00 - 9:00"),
    ("9:00 - 10:00", "9:00 - 10:00"),
    ("10:00 - 11:00", "10:00 - 11:00"),
    ("11:00 - 12:00", "11:00 - 12:00"),
    ("12:00 - 13:00", "12:00 - 13:00"),
    ("13:00 - 14:00", "13:00 - 14:00"),
    ("14:00 - 15:00", "14:00 - 15:00"),
    ("15:00 - 16:00", "15:00 - 16:00"),
    ("16:00 - 17:00", "16:00 - 17:00"),
    ("17:00 - 18:00", "17:00 - 18:00"),
    ("18:00 - 19:00", "18:00 - 19:00"),
    ("19:00 - 20:00", "19:00 - 20:00"),
)

estado_cita = (
    ("terminada", "terminada"),
    ("cancelado", "cancelado"),
    ("agendado", "agendado"),


)

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=150)
    marca = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to = 'productos', null=True, blank=True )
    
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    
    cedula = models.IntegerField()
    correo = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to = 'clientes', null=True, blank=True)
    user = models.OneToOneField(User, models.PROTECT)

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
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    icono = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to = 'servicios', null=True, blank=True)
    
    def __str__(self):
        return self.nombre


class Cita(models.Model):
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=15, choices=horarios)
    estado_cita = models.CharField(max_length=50, default="agendado")
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    barbero = models.ForeignKey(Barbero, on_delete=models.PROTECT)
    servicios = models.ManyToManyField(Servicio, blank=True)
    

    def __str__(self):
        return str(self.fecha_creacion)