from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length =50)
    modelo = models.CharField(max_length =50)
    anio = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} {self.anio}'

# Create your models here.
