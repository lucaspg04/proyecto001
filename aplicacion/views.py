from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import crearCuenta

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registration/registro.html')

def crearcuenta(request):
    form=crearCuenta()
    contexto={
        "form":form
    }

    if request.method=="POST":
        form=crearCuenta(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
        
    return render(request,"registration/crearcuenta.html",contexto)