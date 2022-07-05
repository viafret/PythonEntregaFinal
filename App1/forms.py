from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class IntegrantesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    profesion = forms.CharField()

class ProductoForm(forms.Form):

    nombre = forms.CharField (max_length=40)
    precio = forms.IntegerField()
    stock = forms.BooleanField()

class ContactoForm(forms.Form):

    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField ()
    telefono = forms.IntegerField ()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField(label = 'Apellido')
    first_name = forms.CharField(label = 'Nombres')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label = "Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required = False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required = False)

    last_name = forms.CharField(label = 'Modificar el apellido')
    first_name = forms.CharField(label = 'Modificar los nombres')
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts={k:"" for k in fields}