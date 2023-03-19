from django.shortcuts import render
from django.http import HttpResponse
from develop.models import *
from develop.forms import *

def inicio(request):
    return render(request, "develop/inicio.html")

def libros(request):
    data = {
        'form': LeidosFormulario()
    }
    
    if request.method == "POST":
        formulario = LeidosFormulario(data=request.POST)
        if formulario.is_valid:
            formulario.save()
        else: 
            data["form"] = formulario
    
    return render(request, 'develop/LeidosForm.html', data)

def libros_vender(request):
    data = {
        'form': VenderFormulario()
    }
    
    if request.method == "POST":
        formulario = VenderFormulario(data=request.POST)
        if formulario.is_valid:
            formulario.save()
        else: 
            data["form"] = formulario
    
    return render(request, 'develop/SellForm.html', data)

def libros_comprar(request):
    data = {
        'form': ComprarFormulario()
    }
    
    if request.method == "POST":
        formulario = ComprarFormulario(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = 'Información enviada'
        else: 
            data["form"] = formulario
    
    return render(request, 'develop/BuyForm.html', data)

def buscarLibro(request):
    return render(request, 'develop/ListaLibrosBuy.html')

def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        precio = Libro_buy.objects.filter(titulo__icontains=titulo)
        
        return render(request, "develop/resultadosbusqueda.html", {"titulo": titulo, "precio": precio})
    
    else:
        respuesta = "No enviaste datos"
        
    return HttpResponse(respuesta)
