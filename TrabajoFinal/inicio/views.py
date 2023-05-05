from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    print (request.method)

    context = { }
    return render (request, 'inicio/index.html', context)

def menu(request):
    return HttpResponse("Aca va listado del menu")

def nosotros(request):
    return HttpResponse(f"Quiene somos y sucursales")

def contacto(request):
    return HttpResponse(f"Formulario de contacto y link de Wpp")