from django.urls import path
from . import views  # Importa las vistas de la app

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de que "home" esté definido en views.py
]
