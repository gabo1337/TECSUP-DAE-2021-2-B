from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField( max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) :
        return self.nombre

class Producto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField( max_length=200)
    precio = models.DecimalField( max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField( max_length=200)
    apellido = models.CharField( max_length=200)
    telefono = models.CharField( max_length=200)
    direccion = models.CharField( max_length=200)
    email = models.EmailField( max_length=254)
    fechaNacimiento = DateTimeField("Fecha de nacimiento")
    pub_date = DateTimeField(auto_now=True,verbose_name="date published")

    def __str__(self):
        return self.nombre