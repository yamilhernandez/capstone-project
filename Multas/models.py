from django.db import models
from Casos.models import Caso
from Agencias.models import Agencia
import uuid

# Create your models here.
 
class Infraccion(models.Model):
    id_infraccion = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    aviso = models.IntegerField()
    primera_multa = models.IntegerField()
    segunda_multa = models.IntegerField()
    tercera_multa = models.IntegerField()
    
    def __str__(self):
        return self.descripcion
    
    
class Multa(models.Model):
    multa_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    nombre_agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    num_caso = models.ForeignKey(Caso, on_delete=models.CASCADE, blank=True, null=True)
    total = models.CharField(max_length=60,  blank=False)
    infraccion = models.ForeignKey(Infraccion, on_delete=models.CASCADE)
    pago = models.BooleanField(null=True, blank=True)
    infraccion_count = models.IntegerField(default=0)
    

class MultasAprobada(models.Model):
    multa_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    nombre_agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    num_caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    total = models.CharField(max_length=60,  blank=False)
    infraccion = models.ForeignKey(Infraccion, on_delete=models.CASCADE)
    pago = models.BooleanField(null=True, blank=True)
    infraccion_count = models.IntegerField(default=0)