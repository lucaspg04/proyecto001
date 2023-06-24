from django.db import models

# Create your models here.

class Producto(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=300)
    precio=models.IntegerField()
    stock=models.IntegerField()
    imagen=models.ImageField(upload_to="productos")

