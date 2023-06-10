from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
