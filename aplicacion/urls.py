from django.contrib import admin
from django.urls import path
from .views import index, registro, registro, Admproductos,  crearproducto, updateProducto, \
    deleteProducto, productosuser, crearpedido, ver_producto, pedidoreali, listar, marca_categoria, \
    carrito, crearmarca, crearcategoria, productos_mujer, productos_hombre, categoria_hombre, categoria_mujer, \
    modificarmarca, modificarcategoria, eliminarcategoria, eliminarmarca
    
urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('admProductos', Admproductos, name="admProductos"),
    path('crearproducto', crearproducto, name="crearproducto"),
    path('updateproducto/<id>', updateProducto, name="updateproducto"),
    path('deleteproducto/<id>', deleteProducto, name="deleteproducto"),
    path('productosuser', productosuser, name="productosuser"),
    path('accounts/registro',registro,name="registro"),
    path('pedido', crearpedido, name="crearpedido"),
    path('verproducto/<id>', ver_producto, name="verproducto"),
    path('pedidorealizado', pedidoreali, name="pedidorealizado"),
    path('listar', listar, name="listar"),
    path('marca_categorias', marca_categoria, name='marca_categoria'),
    path('carrito', carrito, name="carrito"),
    path('crearmarca', crearmarca, name="crearmarca"),
    path('modificarmarca/<int:id>', modificarmarca, name="modificarmarca"),
    path('modificarcategoria/<int:id>', modificarcategoria, name="modificarcategoria"),
    path('eliminarmarca/<int:id>', eliminarmarca, name="eliminarmarca"),
    path('eliminarcategoria/<int:id>', eliminarcategoria, name="eliminarcategoria"),
    path('crearcategoria', crearcategoria, name="crearcategoria"),
    path('productosmujer' , productos_mujer, name="productosmujer"),
    path('productoshombre' , productos_hombre, name="productoshombre"),
    path('hombrecategoria/<str:categoria>/', categoria_hombre, name="hombrecategoria"),
    path('mujercategoria/<str:categoria>/', categoria_mujer, name="mujercategoria"),
]