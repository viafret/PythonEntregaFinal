from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
#class Familia(models.Model):

 #   nombre = models.CharField(max_length=40)
  #  edad = models.IntegerField()
  #  fechaNac = models.DateField()

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