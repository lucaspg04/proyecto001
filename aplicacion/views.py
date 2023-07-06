from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import frmRegistro, frmCrearProducto, frmCrearCategoria, frmCrearMarca
from .models import Producto, Pedido, DetallePedido, Categoria, Marca
from carro.carro import Carro
from django.contrib import messages
from django.db import transaction
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

def carrito(request):
    return render(request, 'carro/carrito.html')

def listar(request):
    
    pedidos = Pedido.objects.all()
    detalles = DetallePedido.objects.all()
    
    contexto = {
        'pedido':pedidos,
        'detalle':detalles
    }
    
    return render(request, 'aplicacion/pedidos/listar.html', contexto)

def marca_categoria(request):
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()
    
    contexto = {
        'marca':marcas,
        'categoria':categorias
    }
    
    return render(request, "aplicacion/marca_categoria/marca_categoria.html", contexto)

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

def crearmarca(request):
    
    form = frmCrearMarca(request.POST or None)
    
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
            return redirect(to="marca_categoria")    
        
    return render(request, 'aplicacion/marca_categoria/crearmarca.html', contexto)

def crearcategoria(request):
    
    form = frmCrearCategoria(request.POST or None)
    
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
            return redirect(to="marca_categoria")    
        
    return render(request, 'aplicacion/marca_categoria/crearcategoria.html', contexto)

def modificarmarca(request,id):
    
    marca = get_object_or_404(Marca, id=id)
    
    contexto={
        'form': frmCrearMarca(instance=marca)
    }
    
    if request.method == 'POST':
        formulario = frmCrearMarca(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="marca_categoria")    
    return render(request,"aplicacion/marca_categoria/modificarmarca.html", contexto)

def modificarcategoria(request,id):
    
    categoria = get_object_or_404(Categoria, id=id)
    
    contexto={
        'form': frmCrearCategoria(instance=categoria)
    }
    
    if request.method == 'POST':
        formulario = frmCrearCategoria(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="marca_categoria")    
    return render(request,"aplicacion/marca_categoria/modificarcategoria.html", contexto)

def eliminarmarca(request,id):
    
    marca=get_object_or_404(Marca,id=id)
    contexto={
        "prod":marca
    }

    if request.method=="POST":
        marca.delete()
        return redirect(to="marca_categoria")

    return render(request,"aplicacion/marca_categoria/eliminarmarca.html",contexto)

def eliminarcategoria(request,id):
    
    categoria=get_object_or_404(Categoria,id=id)
    contexto={
        "prod":categoria
    }

    if request.method=="POST":
        categoria.delete()
        return redirect(to="marca_categoria")

    return render(request,"aplicacion/marca_categoria/eliminarcategoria.html",contexto)

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

def productos_mujer(request):
    
    productos= Producto.objects.filter(genero="F")
    
    contexto={
        'productos': productos
    }
    
    return render(request, 'aplicacion/producto_mujer/productos_mujer.html', contexto)

def categoria_mujer(request, categoria):
    
    categoria = Categoria.objects.get(nombre=categoria)
    productos= Producto.objects.filter(genero="F", categoria=categoria)
    
    contexto={
        'productos': productos
    }
    
    return render(request, 'aplicacion/producto_mujer/categoria_mujer.html', contexto)

def productos_hombre(request):
    
    productos= Producto.objects.filter(genero="M")
    
    contexto={
        'productos': productos
    }
    
    return render(request, 'aplicacion/producto_hombre/productos_hombre.html', contexto)

def categoria_hombre(request, categoria):
    
    categoria = Categoria.objects.get(nombre=categoria)
    productos = Producto.objects.filter(genero='M', categoria=categoria)
    contexto = {
        'productos': productos
    }
    
    return render(request, 'aplicacion/producto_hombre/categoria_hombre.html', contexto)


@login_required
def crearpedido(request):
    carro = Carro(request)
    pedido = Pedido.objects.create(user=request.user)
    total_monto = 0

    for key, value in carro.carro.items():
        producto = Producto.objects.get(id=key)
        cantidad = value["cantidad"]
        precio = producto.precio

        producto.stock -= cantidad
        producto.save()

        DetallePedido.objects.create(
            producto=producto,
            cantidad=cantidad,
            user=request.user,
            pedido=pedido
        )

        total_monto += precio * cantidad

    pedido.monto_total = total_monto
    pedido.save()

    carro.vaciar()

    return render(request, 'aplicacion/pedidorealizado.html')

