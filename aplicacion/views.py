from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import frmRegistro, frmCrearProducto
from .models import Producto, Pedido, DetallePedido
from carro.carro import Carro
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    carro=Carro(request)
    
    productos=Producto.objects.all()
    
    contexto= {'prod':productos}
    
    return render(request, 'aplicacion/index.html', contexto)

def pedidoreali(request):
    return render(request, 'aplicacion/pedidorealizado.html')

def registro(request):
    return render(request, 'registration/registro.html')

def Admproductos(request):
    productos = Producto.objects.all()
    contexto = {'prod': productos}
    return render(request, 'aplicacion/productos/productos.html', contexto)

def crearproducto(request):
    
    form=frmCrearProducto(request.POST, request.FILES or None)

    contexto={
        "form":form
    }

    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="admProductos")
            
    return render(request, 'aplicacion/productos/crear.html', contexto)

def updateProducto(request,id):
    
    producto = get_object_or_404(Producto, id=id)
    
    contexto={
        'form': frmCrearProducto(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = frmCrearProducto(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admProductos")    
    return render(request,"aplicacion/productos/update.html", contexto)

def deleteProducto(request,id):
    
    producto=get_object_or_404(Producto,id=id)
    contexto={
        "prod":producto
    }

    if request.method=="POST":
        producto.delete()
        return redirect(to="admProductos")

    return render(request,"aplicacion/productos/delete.html",contexto)

def registro(request):
    contexto={
        "form": frmRegistro
    }
    
    if request.method == 'POST':
        formulario = frmRegistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
            return render(request, 'registration/registro.html', contexto)
    return render(request, 'registration/registro.html', contexto)


def productosuser(request):
    
    productos=Producto.objects.all()
    
    contexto= {'prod':productos}
    
    return render(request, 'aplicacion/productouser.html', contexto)

def ver_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    contexto = {'prod': producto}
    return render(request, 'aplicacion/verproducto.html', contexto)

def crearpedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    detalle_pedido=[]
    for key, value in carro.carro.items():
        detalle_pedido.append(DetallePedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    
    DetallePedido.objects.bulk_create(detalle_pedido)
    
    return render(request, 'aplicacion/pedidorealizado.html')