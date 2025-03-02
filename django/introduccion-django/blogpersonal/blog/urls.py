# Django
from django.urls import path

# Views
from . import views

# Config
urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.post, name='post'),
]