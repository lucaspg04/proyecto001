from django.contrib import admin
from django.urls import path
from .views import index, registro, registro, Admproductos,  crearproducto
urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('admProductos', Admproductos, name="admProductos"),
    path('crearproducto', crearproducto, name="crearproducto"),
    path('accounts/registro',registro,name="registro"),
    
]