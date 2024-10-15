from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    email = models.EmailField()
    prioridad = models.IntegerField()
