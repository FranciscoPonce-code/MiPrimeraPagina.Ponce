from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('reservas/', views.reservas, name='reservas'),
    path('nuevo_plato/', views.nuevo_plato, name='nuevo_plato'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('buscar/', views.buscar_plato, name='buscar_plato'),
    path('reservas/', views.reservas, name='reservas'),
    path('reserva_exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
    path('login/', views.login_view, name='login'), # Agrega login
    path('registrarse/', views.register_view, name='registrarse'), 
    path('logout/', views.logout_view, name='logout'),
    path('Reseñas/', views.lista_Reseñas, name='lista_Reseñas'),
    path('Reseñas/escribir/', views.escribir_Reseña, name='escribir_Reseña'),
]