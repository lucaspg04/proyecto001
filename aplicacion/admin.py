from django.contrib import admin
from .models import Producto, Pedido, DetallePedido, Marca, Categoria
from carro.carro import Carro

# Register your models here.

class admproducto(admin.ModelAdmin):
    list_display=["id", "marca" ,"nombre", "categoria", "descripcion", "precio", "stock", "genero", "imagen"]
    list_editable=["nombre", "categoria", "marca", "descripcion", "precio", "stock", "genero" , "imagen"]

    class meta:
        model=Producto
        
        
    
class admpedido(admin.ModelAdmin):
    list_display=["id", "User", "creado_en"]

admin.site.register(Producto, admproducto)
admin.site.register([Pedido, DetallePedido])
admin.site.register(Marca)
admin.site.register(Categoria)