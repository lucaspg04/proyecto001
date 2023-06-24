from django.contrib import admin
from .models import Producto

# Register your models here.

class admproducto(admin.ModelAdmin):
    list_display=["id", "nombre", "descripcion", "precio", "stock", "imagen"]
    list_editable=["nombre", "descripcion", "precio", "stock", "imagen"]

    class meta:
        model=Producto

admin.site.register(Producto, admproducto)