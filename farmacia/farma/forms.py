from django import forms
from django.forms import ModelForm
from .models import*

class Producto_Form(ModelForm):
    class Meta:
        model =   Productos
        fields =  ['NomProducto', 'precio', 'descripcion' ,'categoria',]