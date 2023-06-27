from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import frmRegistro, frmCrearProducto
from .models import Producto
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    
    productos=Producto.objects.all()
    
    contexto= {'prod':productos}
    
    return render(request, 'aplicacion/index.html', contexto)

def registro(request):
    return render(request, 'registration/registro.html')

def Admproductos(request):
    
    productos=Producto.objects.all()
    
    contexto= {'prod':productos}
    
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
        
    return render(request, 'registration/registro.html', contexto)


def productosuser(request):
    
    productos=Producto.objects.all()
    
    contexto= {'prod':productos}
    
    return render(request, 'aplicacion/productouser.html', contexto)