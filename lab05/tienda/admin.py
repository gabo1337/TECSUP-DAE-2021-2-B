from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto,Cliente

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Producto)