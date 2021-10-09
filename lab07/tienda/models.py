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
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.nombre

class Registro_Pedidos(models.Model):
    nombre = models.CharField( max_length=200)
    precio = models.DecimalField( max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.nombre

class Registro_Pedidos_User(models.Model):
    precio = models.DecimalField( max_digits=6, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    pub_date = DateTimeField("date published")

