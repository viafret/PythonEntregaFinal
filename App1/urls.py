from re import L
from django import views
from django.urls import path
from App1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('integrantes/', views.integrantes, name="Integrantes"),
    #path('actividades/', views.actividades, name="Actividades"),
    path('producto/', views.producto, name="Producto"),
    path('contacto/', views.contacto, name="Contacto"),
    #path('integrantesForm/', views.integrantesForm, name="integrantesForm"),
    path('buscarIntegrante/', views.buscarIntegrante, name="buscarIntegrante"),
    path('buscar/', views.encontrarInt),
    path('leerIntegrantes/', views.leerIntegrantes, name="LeerIntegrantes"),
    path('eliminarIntegrante/<apellido>/', views.borrarIntegrante, name="EliminarInt"),
    path('editarIntegrante/<apellido>/', views.editarIntegrante, name="EditarInt"),
    #CRUD Productos
    path('productos/lista/', views.ProductoList.as_view(), name='productos_lista'),
    path('productos/<pk>', views.ProductoDetalle.as_view(), name='productos_detalle'),
    path('productos/nuevo/', views.ProductoCrear.as_view(), name='productos_crear'),
    path('productos/edicion/<pk>', views.ProductoEditar.as_view(), name='productos_editar'),
    path('productos/borrar/<pk>', views.ProductoEliminar.as_view(), name='productos_borrar'),
    #LOGIN
    path('login', views.pedidoLog, name = 'Login'),
    #REGISTRO
    path('registro', views.registro, name = 'Registro'),
    #LOGOUT
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),

    ]   