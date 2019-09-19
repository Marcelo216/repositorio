from django.contrib import admin

# Register your models here.

from models import Persona, Producto, Compra

admin.site.register(Persona)

admin.site.register(Producto)

admin.site.register(Compra)
