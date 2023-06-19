from django.db import models

# Create your models here.

class producto(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    descripcion=models.TextField(max_length=300)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    imagen=models.ImageField()

