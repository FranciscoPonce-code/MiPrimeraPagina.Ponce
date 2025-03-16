from django.shortcuts import render, redirect
from .models import Plato, Reserva, Cliente  # noqa: F401
from .forms import PlatoForm, ReservaForm, ClienteForm, BuscarPlatoForm

def index(request):
    return render(request, 'miapp/index.html')

def menu(request):
    platos_del_dia = Plato.objects.filter(es_plato_del_dia=True)
    return render(request, 'miapp/menu.html', {'platos_del_dia': platos_del_dia})

def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    return render(request, 'miapp/reservas.html', {'form': form})

def reserva_exitosa(request):
    return render(request, 'miapp/reserva_exitosa.html')

def nuevo_plato(request):
    form = PlatoForm()
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    return render(request, 'miapp/nuevo_plato.html', {'form': form})

def nuevo_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'miapp/nuevo_cliente.html', {'form': form})

def buscar_plato(request):
    resultados = []
    form = BuscarPlatoForm()
    if request.method == 'GET':
        form = BuscarPlatoForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Plato.objects.filter(nombre__icontains=termino)
    return render(request, 'miapp/buscar.html', {'form': form, 'resultados': resultados})