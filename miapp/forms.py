from django import forms
from .models import Plato, Reserva, Cliente

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BuscarPlatoForm(forms.Form):
    termino = forms.CharField(label="Buscar plato", max_length=100)