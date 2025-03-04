from django.shortcuts import render, HttpResponse

# Importando el modelo
from .models import Project

# Create your views here.
def profile(request):
    projects = Project.objects.all()
    return HttpResponse(projects)