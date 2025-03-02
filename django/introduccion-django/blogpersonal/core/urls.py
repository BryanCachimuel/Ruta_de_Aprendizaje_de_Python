# Django
from django.urls import path

# Views
from . import views

# Config
urlpatterns = [
    path('', views.index, name='home')
]