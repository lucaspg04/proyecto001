from django.contrib import admin
from django.urls import path
from .views import index, registro, crearcuenta

urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('accounts/registro',crearcuenta,name="registro")
]