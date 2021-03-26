from django.shortcuts import render

# Create your views here.

def vista_equipo(request):
    return render(request, 'equipo.html')

def vista_inicio(request):
    return render(request,'inicio.html')

def vista_servicio(request):
    return render(request,'servicio.html')

def vista_productos(request):
    return render(request,'productos.html')

def vista_contacto(request):
    return render(request,'contacto.html')

def vista_registro(request):
    return render(request,'registro.html')

def vista_inicio_sesion(request):
    return render(request,'inicio_sesion.html')

def vista_solicitar_cita(request):
    return render(request,'solicitar_cita.html')

        
    



    
