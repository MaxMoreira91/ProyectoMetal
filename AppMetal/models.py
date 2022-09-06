from pyexpat import model
from django.db import models

class Ingresantes(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido
    
class Graduados(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre+" "+self.apellido

class Bandas(models.Model):
    nombre= models.CharField(max_length=50)
    comision= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.comision)