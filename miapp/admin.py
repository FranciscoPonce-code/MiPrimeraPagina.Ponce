from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', )  # Corrección aquí
    list_filter = ('fecha',)
    search_fields = ('nombre',)