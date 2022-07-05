from pickletools import read_unicodestring1
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Integrantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Profesión: {self.profesion}"
class Contacto(models.Model):

    nombre = models.CharField (max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField ()
    telefono = models.IntegerField ()

class Producto(models.Model):

    nombre = models.CharField (max_length=40)
    precio = models.IntegerField()
    stock = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio} - Stock: {self.stock}"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)