
from django.http import request
from django.shortcuts import redirect, render
from .models import Barbero
from .forms import *

# Create your views here.


def vista_equipo(request):
    return render(request, 'equipo.html')


def vista_inicio(request):
    return render(request, 'inicio.html')


def vista_servicio(request):  # traer informacion de la base datos, consultas

    nombre = ["mateo Barber", "alex Barber"]
    serv = ["corte clasico", "limpieza facial", "barba", "coloracion"]
    return render(request, 'servicio.html', locals())


def vista_productos(request):
    return render(request, 'productos.html')


def vista_contacto(request):
    info_enviado=False
    mail = ""
    subj = ""
    text = ""

    if request.method == "POST":
        formulario = contacto_form (request.POST)
        if formulario.is_valid():
            info_enviado=True
            mail = formulario.clean_data['Correo']
            subj = formulario.clean_data['asunto']
            text = formulario.clean_data['texto']

        
            
    formulario = contacto_form()
        
    return render(request,'contacto.html', locals())

def vista_registro(request):
    return render(request,'registro.html')


def vista_inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def vista_solicitar_cita(request):
    return render(request,'solicitar_cita.html')

# vistas barbero
def listar_barbero (request):
    lista = Barbero.objects.filter()
    return render(request, 'listar_barbero.html',locals())


def agregar_barbero (request):
    if request.method == 'POST':
        formulario = agregar_barbero_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar_barbero/')
            
    else:
        formulario = agregar_barbero_form()

    return render(request, 'agregar_barbero.html',locals())


def editar_barbero (request, id_br):

    var1 = Barbero.objects.get(id=id_br)
    if request.method == "POST":
        formulario = agregar_barbero_form(request.POST, request.FILES, instance=var1)
        if formulario.is_valid():
            var1 = formulario.save()
            return redirect ('/listar_barbero/')
    else:
        formulario = agregar_barbero_form(instance = var1)

    return render(request, 'editar_barbero.html',locals())


def eliminar_barbero (request):
    
    return render(request, 'eliminar_barbero.html',locals())



    
