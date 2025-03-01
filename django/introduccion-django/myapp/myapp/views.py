from django.http import HttpResponse

def saludar(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',')]
    print(numeros)
    numeros_ordenados = sorted(numeros)
    print(request.GET)
    return HttpResponse(str(numeros_ordenados))

def verificar(request, nombre, edad):
    if edad < 12:
        mensaje = f'Hola, {nombre} perdon pero no puede ingresar a está página'
    else:
        mensaje = f'Hola, {nombre} si puedes ingresar a está página'

    return HttpResponse(mensaje)
