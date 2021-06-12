
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.





def vista_inicio(request):
    return render(request, 'inicio.html')


#def vista_servicio(request):  # traer informacion de la base datos, consultas

    #nombre = ["mateo Barber", "alex Barber"]
    #serv = ["corte clasico", "limpieza facial", "barba", "coloracion"]
    #return render(request, 'servicio.html', locals())



def vista_inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def vista_equipo(request):
    return render (request,'equipo.html')

def vista_servicios(request):
    return render (request,'servicios.html')

def vista_agenda(request):
    return render (request,'agenda.html')

def vista_index(request):
    return render (request,'index.html')

def vista_registrate(request):
    return render (request,'registrate.html')






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



#vista login
def vista_login (request):
    usu = ""
    cla = ""
    if request.method == "POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                msj = "usuario o clave incorrectos"

        formulario = login_form()
        return render(request, 'login.html', locals())


def vista_logout (request):
    logout(request)
    return redirect('/login/')


def vista_login(request):
    return render (request,'login.html')

