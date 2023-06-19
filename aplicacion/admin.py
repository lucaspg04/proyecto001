from django.contrib import admin
from .models import producto

# Register your models here.

class admproducto(admin.ModelAdmin):
    list_display=["id", "nombre", "descripcion", "precio", "cantidad", "imagen"]
    list_editable=["nombre", "descripcion", "precio", "cantidad", "imagen"]

    class meta:
        model=producto

admin.site.register(producto, admproducto)