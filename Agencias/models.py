
import uuid
from django.db import models
#from simple_history.models import HistoricalRecords
from datetime import datetime
from Usuarios.models import Usuario
# Create your models here.


#my_choices = (('True', 'Cumplimiento'), ('False', 'Incumplimiento'))
agencias_nombre = ()
tipo_ref = (('DEL', 'Delegada'), ('EXE', 'Exenta'))


class Agencia(models.Model):

    agencia_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    acronimo = models.CharField(max_length=30, blank=False)
    nombre = models.CharField(max_length=60, blank=False)
    categoria = models.CharField(
        max_length=30, choices=tipo_ref, default=('', ''), blank=False)
    tipo = models.CharField(max_length=1000, default='', blank=False)
    fecha_inicio = models.DateField(blank=False)
    fecha_final = models.DateField(blank=False)
    oficial = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    image_agencia = models.ImageField(
        upload_to='agencia', blank=False, null=False)

    alerta = models.BooleanField(
        blank=False, default='False')
    #history = HistoricalRecords()
    #dropdown = models.CharField(max_length=20, choices=my_choices,default='Cumplimiento' if alerta else 'Incumplimiento')
    #numero_compras = models.SlugField(primary_key=True, max_length=30, default='')

    def __str__(self):
        return self.acronimo
