from django.shortcuts import render
from django.http import HttpResponse

from .forms import PedidoForm

def index (request):
    print (request.method)

    context = { }
    return render (request, 'inicio/index.html', context)

def menu(request):
    return HttpResponse("Aca va listado del menu")

def nosotros(request):
    return HttpResponse(f"Quiene somos y sucursales")

def pedido(request):
    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
    else:
        pedido_form = PedidoForm()
    
    context = {
        'form': pedido_form
    }

    return render(request, 'inicio/pedido.html', context)