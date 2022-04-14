from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField()
    deporte = models.CharField(max_length=40)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    area = models.CharField(max_length=30)

class Deporte(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.BooleanField()