from django import forms
from .models import Plato, Reserva, Cliente, Reseña

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        help_texts = {"username": ""}

class BuscarPlatoForm(forms.Form):
    termino = forms.CharField(label="Buscar plato", max_length=100)

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['titulo', 'contenido', 'calificacion']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 5}),
            'calificacion': forms.RadioSelect(choices=Reseña.calificacion.field.choices),
        }