from django.urls import path
from . import views
from django.urls import path
from .views import Startstrona, przywroc_stan
urlpatterns = [

    path('', views.Startstrona, name='Startstrona'),
    path('Startstrona/', views.Startstrona, name='Startstrona'),
path('przywroc_stan/<int:stan_id>/', przywroc_stan, name='przywroc_stan_url'),  # Nowa ścieżka
]