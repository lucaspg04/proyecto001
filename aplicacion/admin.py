from django.contrib import admin
from .models import Producto, Pedido, DetallePedido
from carro.carro import Carro

# Register your models here.

class admproducto(admin.ModelAdmin):
    list_display=["id", "nombre", "descripcion", "precio", "stock", "imagen"]
    list_editable=["nombre", "descripcion", "precio", "stock", "imagen"]

    class meta:
        model=Producto
        
        
        
class admpedido(admin.ModelAdmin):
    list_display=["id", "User", "creado_en"]

admin.site.register(Producto, admproducto)
admin.site.register([Pedido, DetallePedido])