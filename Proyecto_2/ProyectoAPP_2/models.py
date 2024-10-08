from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tfno = models.IntegerField()

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio= models.IntegerField()

class Pedido(models.Model):
    nropedido=models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

#  python manage.py makemigrations

# python3 manage.py migrate

# DESCARGAR SQLBROWSER https://sqlitebrowser.org/dl/

