# Django
from django.urls import path

# Views
from . import views

# Config
urlpatterns = [
    path('', views.profile, name='profile')
]