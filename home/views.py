
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.
# Vistas principales
def vista_inicio(request):
    productos = Producto.objects.filter(estado=True).order_by('-id')
    servicios = Servicio.objects.filter().order_by('-id')
    return render(request, 'index.html', locals())

def vista_servicios(request):
    servicios = Servicio.objects.filter().order_by('id')
    return render (request,'servicios.html', locals())

def vista_inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def vista_agenda(request):
    return render (request,'agenda.html')

def vista_index(request):
    return render (request,'index.html')
#<-----end_view----->

#vista registrate
def vista_registrate(request):
    if request.method == 'POST':
        usu = ""
        ema = ""
        cla = ""
        
        form_user = user_form(request.POST)
        form_persona = registrate_form(request.POST, request.FILES)
        if form_persona.is_valid() and form_user.is_valid():
            usu = form_user.cleaned_data['username']
            ema = form_user.cleaned_data['email']
            cla = form_user.cleaned_data['password']
            u = User.objects.create_user(username = usu, email = ema, password = cla)

            p = form_persona.save(commit = False)
            p.user = u
            u.save()
            p.save()
            
    else:
        form_user = user_form()
        form_persona = registrate_form()
    return render (request,'registrate.html',locals())
#<-----end_view----->


# vistas barbero
def agregar_barbero (request):
    if request.method == 'POST':
        formulario = agregar_barbero_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/equipo/')
            
    else:
        formulario = agregar_barbero_form()

    return render(request, 'agregar_barbero.html',locals())

def editar_barbero (request, id_br):

    var1 = Barbero.objects.get(id=id_br)
    if request.method == "POST":
        formulario = agregar_barbero_form(request.POST, request.FILES, instance=var1)
        if formulario.is_valid():
            var1 = formulario.save()
            return redirect ('/equipo/')
    else:
        formulario = agregar_barbero_form(instance = var1)

    return render(request, 'editar_barbero.html',locals())


def listar_barbero (request):
    lista = Barbero.objects.filter().order_by('-id')
    return render(request, 'listar_barbero.html',locals())

def eliminar_barbero (request, id_br):
    var2 = Barbero.objects.get(id=id_br)
    var2.delete()
    return redirect ('/equipo/')
    #return render(request, 'eliminar_barbero.html',locals())

def ver_barbero (request, id_Barbero):

    b = Barbero.objects.get(id=id_Barbero)
    
    return render(request, 'ver_barbero.html',locals())
#<-----end_view----->


#vistas servicios
def listar_servicio (request):
    lista = Servicio.objects.filter()
    return render(request, 'listar_servicio.html',locals())


def agregar_servicio (request):
    if request.method == 'POST':
        form_serv = agregar_servicio_form(request.POST, request.FILES)
        if form_serv.is_valid():
            form_serv.save()
            return redirect('/equipo/')
            
    else:
        formulario = agregar_servicio_form()
    
    return render(request, 'agregar_servicio.html',locals())

def editar_servicio (request, id_br):

    var3 = Servicio.objects.get(id=id_br)
    if request.method == "POST":
        form_serv = agregar_servicio_form(request.POST, request.FILES, instance=var3)
        if form_serv.is_valid():
            var3 = form_serv.save()
            return redirect ('/equipo/')
    else:
        form_serv = agregar_servicio_form(instance = var3)

    return render(request, 'editar_servicio.html',locals())


def eliminar_servicio (request, id_br):
    var2 = Servicio.objects.get(id=id_br)
    var2.delete()
    return redirect ('/equipo/')
#<-----end_view----->



    
#vistas CLientes
@login_required (login_url = '/login/')
def agendar_cita (request):
    
    c = Persona.objects.get(user = request.user)

    if request.method == 'POST':
        form_cita = agregar_cita_form(request.POST, request.FILES)
        if form_cita.is_valid():
            f = form_cita.save(commit=False)
            #realizar consultas de agenda
            #usuario realizo una reserva antes de la cita

            #si el barbero esta disponible en el dia y hora

            f.persona = c
            f.save()
            return redirect('/servicios/')
            
    else:
        formulario = agregar_cita_form()

    return render(request, 'crear_cita.html',locals())



#vista login
def vista_login (request):
    usu = ""
    cla = ""
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            usu = form.cleaned_data['usuario']
            cla = form.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                msj = "usuario o clave incorrectos"
    form = login_form()
    return render(request, 'login.html', locals())


def vista_logout (request):
    logout(request)
    return redirect('/login/')

#vistas productos
def crear_producto (request):
    if request.method == 'POST':
        form_prod = crear_prod_form (request.POST, request.FILES)
        if form_prod.is_valid():
            form_prod.save()
            return redirect('/equipo/')
            
    else:
        formulario = crear_prod_form()
    
    return render(request, 'crear_producto.html',locals())
    


