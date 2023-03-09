from django.contrib import admin
from GestionInventarioApp.models import Categoria, Producto

# Register your models here.

class Categoria_admin (admin.ModelAdmin): 
    readonly_fields = ('created','updated')

class Producto_admin (admin.ModelAdmin): 
    readonly_fields = ('created','updated')
    list_display = ('name','price')

admin.site.register(Categoria, Categoria_admin)
admin.site.register(Producto, Producto_admin)