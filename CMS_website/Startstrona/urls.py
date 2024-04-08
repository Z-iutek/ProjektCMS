from django.urls import path
from . import views
from .views import Startstrona

urlpatterns = [
    path('Startstrona/', views.Startstrona, name='Startstrona'),
]