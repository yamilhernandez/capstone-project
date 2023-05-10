import uuid
from django.utils import timezone
from django.db import models
from Agencias.models import Agencia
from Usuarios.models import Usuario


# Create your models here.

# Create your models here.


# from datetime import datetime
# Create your models here.

# agencias_nombre = ()
tipo_ref = (('En Espera', 'En Espera'),
            ('En Proceso', 'En Proceso'), ('Completado', 'Completado'))


class Caso(models.Model):
    caso_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    id_caso = models.CharField(max_length=500, blank=False, unique=True)

    estado = models.CharField(max_length=30, choices=tipo_ref,
                              default=('', ''), blank=False)
    nombre_agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)

    estatus = models.BooleanField(null=True, blank=True)

    fecha_creacion = models.DateTimeField(
        auto_now_add=True)
    # otros campos del modelo...

    def __str__(self):
        return self.id_caso
