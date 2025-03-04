from django.shortcuts import render, HttpResponse

# Importando el modelo
from .models import Post

# Create your views here.
def posts(request):
    blogs = Post.objects.all()
    return HttpResponse(blogs)

def post(request, id):
    blog = Post.objects.get(id=id)
    content = f'{blog.title} - {blog.description}'
    return HttpResponse(content)