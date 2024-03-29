from django.db import models
from django.contrib.auth.models import Group 

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    fk_prov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
Group.objects.get_or_create(name='Cajero')
Group.objects.get_or_create(name='Estudiante')