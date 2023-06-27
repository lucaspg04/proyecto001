from django.contrib import admin
from django.urls import path
from .views import index, registro, registro, Admproductos,  crearproducto, updateProducto, deleteProducto, productosuser

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('admProductos', Admproductos, name="admProductos"),
    path('crearproducto', crearproducto, name="crearproducto"),
    path('updateproducto/<id>', updateProducto, name="updateproducto"),
    path('deleteproducto/<id>', deleteProducto, name="deleteproducto"),
    path('productosuser', productosuser, name="productosuser"),
    path('accounts/registro',registro,name="registro"),
    
]