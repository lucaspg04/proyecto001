from django import forms
from .models import Producto, Marca, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class frmRegistro(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2",]
        
        
class frmCrearProducto(forms.ModelForm):

    class Meta:
        model=Producto
        fields=["nombre", "marca", "categoria","descripcion","precio","stock", "genero",  "imagen"]
        
class frmCrearMarca(forms.ModelForm):
    class Meta:
        model=Marca
        fields=["id", "nombre"]
        
class frmCrearCategoria(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=["id", "nombre"]