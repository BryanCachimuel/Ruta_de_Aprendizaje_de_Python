from django.http import HttpResponse

def saludar(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',')]
    print(numeros)
    numeros_ordenados = sorted(numeros)
    print(request.GET)
    return HttpResponse(str(numeros_ordenados))
