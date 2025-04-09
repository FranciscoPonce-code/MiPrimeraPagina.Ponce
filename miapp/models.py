from django.db import models  # noqa: F401
from django.contrib.auth.models import User
#
from django.db import models  # noqa: F811

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    es_plato_del_dia = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    personas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Reseña(models.Model):  # ¡Esta clase estaba dentro de Cliente!
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    calificacion = models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])

    def __str__(self):
        return f"Reseña de {self.cliente.username}: {self.titulo}"