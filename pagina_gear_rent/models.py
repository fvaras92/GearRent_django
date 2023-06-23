from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Product(models.Model):
    tipoprod = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    imagen= models.ImageField(blank=True, null= True)
    descripcion = models.TextField()
    precio = models.IntegerField()
    oferta = models.IntegerField(blank=True, null= True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

def validate_rut(value):
    rut = value.replace('.', '').replace('-', '').upper()
    rut_number, rut_verifier = rut[:-1], rut[-1]
 
    if not rut_number.isdigit() or len(rut_number) < 7:
        raise ValidationError(_('Rut inválido.'))

class Registro(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, validators=[validate_rut])


__all__ = ['Product', 'Registro']

