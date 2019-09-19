from django.contrib import admin

# Register your models here.

from models import Persona, Producto, Compra

admin.site.register(Persona, Producto, Compra)
