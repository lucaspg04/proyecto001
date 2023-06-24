from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class frmRegistro(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2",]
        
        
class frmCrearProducto(forms.ModelForm):

    class Meta:
        model=Producto
        fields=["nombre","descripcion","precio","stock", "imagen"]