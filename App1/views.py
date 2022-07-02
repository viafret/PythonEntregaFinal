from django.shortcuts import render
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from App1.models import Integrantes, Producto, Contacto
from App1.forms import IntegrantesForm, ProductoForm, ContactoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    return render(request, 'App1/inicio.html') 

def integrantes(request):
    if request.method == 'POST':

        miFormulario = IntegrantesForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            integrante = Integrantes(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],profesion=informacion['profesion'])

            integrante.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = IntegrantesForm()

    return render(request, "App1/integrantes.html", {"miFormulario":miFormulario})


def producto(request):

    if request.method == 'POST':

        miFormulario = ProductoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            producto = Producto(nombre=informacion['nombre'], precio=informacion['precio'], stock=informacion['stock'])

            producto.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = ProductoForm()

    return render(request, "App1/producto.html", {"miFormulario":miFormulario})
    

def contacto(request):

    if request.method == 'POST':

        miFormulario = ContactoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            contacto = Contacto(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])

            contacto.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = ContactoForm()

    return render(request, "App1/contacto.html", {"miFormulario":miFormulario})
    

def buscarIntegrante(request):

    return render(request, "App1/buscarIntegrante.html")

def encontrarInt(request):

    if request.GET["apellido"]:
       
       #respuesta = f"Estoy buscando al integrante de apellido: {request.GET['apellido']}"
        apellido = request.GET['apellido']
        nombres = Integrantes.objects.filter(apellido__icontains=apellido)
    
        return render (request, "App1/resultadoBuscar.html", {"nombres":nombres, "apellido":apellido})

    else:

        respuesta = "No envió datos"

    return HttpResponse(respuesta)

def leerIntegrantes(request):
        
    integrantes = Integrantes.objects.all()

    contexto = {"Integrantes":integrantes}

    return render(request, "App1/leerIntegrantes.html", contexto)

def borrarIntegrante(request, apellido):

    integrante = Integrantes.objects.get(apellido=apellido)
    integrante.delete()

    integrantes = Integrantes.objects.all()

    contexto = {"Integrantes": integrantes}

    return render(request, "App1/leerIntegrantes.html", contexto)

def editarIntegrante(request, apellido):

    integrante = Integrantes.objects.get(apellido=apellido)

    if request.method == 'POST':

        miFormulario = IntegrantesForm(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            integrante.nombre = informacion['nombre']
            integrante.apellido = informacion['apellido']
            integrante.edad = informacion['edad']
            integrante.profesion = informacion['profesion']
            integrante.save()

            return render(request, "App1/inicio.html")
    
    else:

        miFormulario = IntegrantesForm(initial={'nombre': integrante.nombre, 'apellido':integrante.apellido, 'edad':integrante.edad, 'profesion': integrante.profesion})

    
    return render(request, "App1/editarIntegrantes.html", {"miFormulario":miFormulario, "apellido":apellido})

class ProductoList(ListView):
    model = Producto
    template_name = "App1/productos_lista.html"

class ProductoDetalle(DetailView):
    model = Producto
    template_name = "App1/productos_detalle.html"

class ProductoCrear(CreateView):
    model = Producto
    success_url = reverse_lazy('productos_lista')
    fields = ['nombre', 'precio', 'stock']

class ProductoEditar(UpdateView):
    model = Producto
    success_url = reverse_lazy('productos_lista')
    fields = ['nombre', 'precio', 'stock']

class ProductoEliminar(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos_lista')
    fields = ['nombre', 'precio', 'stock']