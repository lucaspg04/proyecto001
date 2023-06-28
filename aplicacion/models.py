from django.db import models

from django.contrib.auth import get_user_model

from django.db.models import Sum, F, FloatField

# Create your models here.

User=get_user_model()

class Producto(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=300)
    precio=models.IntegerField()
    stock=models.IntegerField()
    imagen=models.ImageField(upload_to="productos")
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.detallepedido_set.aggregate(
            
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField)
        )["total"]
        
        
    
    
class DetallePedido(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    creado_en=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'id Pedido: ' + str(self.id) + ', Usuario: ' + str(self.user)