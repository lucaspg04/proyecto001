from django.shortcuts import render
from .carro import Carro
from aplicacion.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=id)
    
    carro.agregar(producto=producto)
    
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=producto)
    
    return redirect("carrito")

def restar_producto(request, id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=id)
    
    carro.restar(producto=producto)
    
    return redirect("carrito")

def limpiar(request, producto_id):
    
    carro=Carro(request)
    
    carro.vaciar()
    
    return redirect("carrito")