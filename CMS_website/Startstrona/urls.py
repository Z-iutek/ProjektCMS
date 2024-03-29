from django.urls import path
from . import views

urlpatterns = [
    path('Startstrona/', views.Startstrona, name='Startstrona'),
]