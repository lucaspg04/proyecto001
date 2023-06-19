from django import forms
from .models import producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class crearCuenta(UserCreationForm):
    class meta:
        model=User
        fields=["username", "email", "password1", "password2"]