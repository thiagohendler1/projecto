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