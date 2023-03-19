from django.urls import path
from develop import views
from develop.views import inicio, libros, libros_comprar, libros_vender, buscarLibro

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('books/', libros, name = "libros"),
    path('buy/', libros_comprar, name = "comprar"),
    path('sell/', libros_vender, name = "vender"),
    path('buscar/', buscarLibro, name = "buscar")
]
