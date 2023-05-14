from django.db import models
from Agencias.models import Agencia
# Create your models here.


class DepoC(models.Model):

    nombre = models.CharField(max_length=60, blank=False)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    email = models.CharField(max_length=1000, default='', blank=False)
    password = models.CharField(max_length=255, blank=False)
