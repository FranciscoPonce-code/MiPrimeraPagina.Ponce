from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('reservas/', views.reservas, name='reservas'),
    path('nuevo_plato/', views.nuevo_plato, name='nuevo_plato'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('buscar/', views.buscar_plato, name='buscar_plato'),
]