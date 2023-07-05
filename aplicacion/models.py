from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models import Sum, F, FloatField

# Create your models here.
genero_choices = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
]

User=get_user_model()

class Marca(models.Model):
    id=models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    id=models.IntegerField(primary_key=True, validators=[MinValueValidator(1)])
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT, null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    descripcion=models.TextField(max_length=300)
    precio=models.IntegerField()
    stock=models.IntegerField(validators=[MinValueValidator(0)])
    genero=models.CharField(null=True, max_length=1, choices=genero_choices)
    imagen=models.ImageField(upload_to="productos")
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en=models.DateTimeField(auto_now_add=True)
    monto_total=models.FloatField(null=True)
    
    def __str__(self):
        return str(self.id)
    
    
class DetallePedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    creado_en=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'id Pedido: ' + str(self.pedido) + ', Usuario: ' + str(self.user)