
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from .forms import *


# Create your views here.





def vista_inicio(request):
    return render(request, 'inicio.html')


#def vista_servicio(request):  # traer informacion de la base datos, consultas

    #nombre = ["mateo Barber", "alex Barber"]
    #serv = ["corte clasico", "limpieza facial", "barba", "coloracion"]
    #return render(request, 'servicio.html', locals())





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

def vista_nosotros(request):
    return render (request,'nosotros.html')


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


def eliminar_barbero (request, id_br):
    var2 = Barbero.objects.get(id=id_br)
    var2.delete()
    return redirect ('/listar_barbero/')

    #return render(request, 'eliminar_barbero.html',locals())


def ver_barbero (request, id_Barbero):

    b = Barbero.objects.get(id=id_Barbero)
    
    return render(request, 'ver_barbero.html',locals())


#vistas servicios
def listar_servicio (request):
    lista = Servicio.objects.filter()
    return render(request, 'listar_servicio.html',locals())


def agregar_servicio (request):
    if request.method == 'POST':
        form_serv = agregar_servicio_form(request.POST, request.FILES)
        if form_serv.is_valid():
            form_serv.save()
            return redirect('/listar_servicio/')
            
    else:
        formulario = agregar_servicio_form()
    
    return render(request, 'agregar_servicio.html',locals())

def editar_servicio (request, id_br):

    var3 = Servicio.objects.get(id=id_br)
    if request.method == "POST":
        form_serv = agregar_servicio_form(request.POST, request.FILES, instance=var3)
        if form_serv.is_valid():
            var3 = form_serv.save()
            return redirect ('/listar_servicio/')
    else:
        form_serv = agregar_servicio_form(instance = var3)

    return render(request, 'editar_servicio.html',locals())


def eliminar_servicio (request, id_br):
    var2 = Servicio.objects.get(id=id_br)
    var2.delete()
    return redirect ('/listar_servicio/')



    
#vistas CLientes
def agendar_cita (request):
    if request.method == 'POST':
        form_cita = agregar_cita_form(request.POST, request.FILES)
        if form_cita.is_valid():
            form_cita.save()
            return redirect('/listar_servicio/')
            
    else:
        formulario = agregar_cita_form()

    return render(request, 'crear_cita.html',locals())