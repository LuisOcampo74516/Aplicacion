from msilib.schema import Class
from django.db import models


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False)
    NomCategoria = models.TextField(max_length=15, null=True, blank=True, name='NomCategoria')

    def __str__ (self):
        return self.NomCategoria


        
class Productos(models.Model):
    NomProducto = models.TextField(max_length=15, null=True, blank=True, name='NomProducto')
    descripcion = models.TextField(max_length=30, null= True)
    precio = models.DecimalField(max_digits = 8, decimal_places = 2)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__ (self):
        return self.NomProducto


# Create your models here.
