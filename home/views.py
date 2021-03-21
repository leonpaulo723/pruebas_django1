from django.shortcuts import render

# Create your views here.

def vista_about(request):
    return render(request, 'about.html')

def vista_contact(request):
    return render(request,'contact.html')
