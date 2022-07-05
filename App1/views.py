from django.shortcuts import render
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from App1.models import Integrantes, Producto, Contacto
from App1.forms import IntegrantesForm, ProductoForm, ContactoForm, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Vistas por funciones

def inicio(request):

    return render(request, 'App1/inicio.html') 

def acercaDe(request):

    return render(request, 'App1/acerca_de.html')

@login_required
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

@login_required
def borrarIntegrante(request, apellido):

    integrante = Integrantes.objects.get(apellido=apellido)
    integrante.delete()

    integrantes = Integrantes.objects.all()

    contexto = {"Integrantes": integrantes}

    return render(request, "App1/leerIntegrantes.html", contexto)

@login_required
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

#Vistas por clases
class ProductoList(LoginRequiredMixin, ListView):
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

#LOGIN
def pedidoLog(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render (request, 'App1/inicio.html', {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render (request, 'App1/inicio.html', {"mensaje":"Error, verifique los datos ingresados"})

        else:

            return render (request, 'App1/inicio.html', {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render (request, 'App1/login.html', {"form":form})

#REGISTRO
def registro(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data ['username']
            form.save()
            return render(request, 'App1/inicio.html', {"mensaje":"Usuario Creado"})

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'App1/registro.html', {"form":form})

#EDITAR USUARIO
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "App1/inicio.html", {'mensaje':'Datos modificados exitosamente'})

    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "App1/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})




