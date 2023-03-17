from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "develop/inicio.html")

def libros(request):
    return render(request, "develop/libros.html")

def libros_comprar(request):
    return render(request, "develop/libros_comprar.html")

def libros_vender(request):
    return render(request, "develop/libros_vender.html")
