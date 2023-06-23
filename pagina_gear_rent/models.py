from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    tipoprod = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    imagen= models.ImageField(blank=True, null= True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
