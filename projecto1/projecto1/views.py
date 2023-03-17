from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola Django - Coder")

def coder(request):
    return HttpResponse("coder me sirvió xd")

def cuentas(request):
    a = 4
    b = 4
    resultado = a + b
    return HttpResponse(f"Este es el resultado: {resultado}")
