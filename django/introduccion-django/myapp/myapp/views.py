from django.http import HttpResponse

def saludar(request):
    print(request)
    print(request.GET)
    return HttpResponse(request.GET['numeros'])
