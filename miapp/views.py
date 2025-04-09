from django.shortcuts import render, redirect
from .models import Plato, Reserva, Cliente  # noqa: F401
from .forms import PlatoForm, ReservaForm, ClienteForm, BuscarPlatoForm, ReseñaForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Reseña 

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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'miapp/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = UserCreationForm()
    return render(request, 'miapp/registrarse.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def lista_Reseñas(request):
    Reseñas = Reseña.objects.all().order_by('-fecha_creacion')
    return render(request, 'miapp/lista_Reseñas.html', {'Reseñas': Reseñas})

@login_required
def escribir_Reseña(request):
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            Reseña = form.save(commit=False)
            Reseña.cliente = request.user
            Reseña.save()
            return redirect('lista_Reseñas')  # Redirige a la lista de reseñas
    else:
        form = ReseñaForm()
    return render(request, 'miapp/escribir_Reseña.html', {'form': form})