
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.





def vista_inicio(request):
    return render(request, 'inicio.html')


def vista_servicio(request):  # traer informacion de la base datos, consultas

    nombre = ["mateo Barber", "alex Barber"]
    serv = ["corte clasico", "limpieza facial", "barba", "coloracion"]
    return render(request, 'servicio.html', locals())





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




def vista_inicio_sesion(request):
    return render(request,'inicio_sesion.html')


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


def editar_barbero (request, id_Barbero):

    var1 = Barbero.objects.get(id=id_Barbero)
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


def ver_barbero (request, id_Barbero):

    b = Barbero.objects.get(id=id_Barbero)
    
    return render(request, 'ver_barbero.html',locals())



def listar_servicios (request):
    lista = Servicio.objects.filter()
    return render(request, 'listar_servicios.html',locals())


def agregar_servicios (request):
    if request.method == 'POST':
        formulario = agregar_servicio_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar_servicios/')
            
    else:
        formulario = agregar_servicio_form()
    
    return render(request, 'agregar_servicios.html',locals())





    
