from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
import uuid

#from datetime import datetime
# Create your models here.

#agencias_nombre = ()
tipo_ref = (('Admin', 'Administrador'),
            ('IT', 'Tecnico'), ('Oficial', 'Oficial'))


class Usuario(AbstractUser):
    usuario_id = models.CharField(max_length=200, unique=True, default=uuid.uuid4)
    puesto = models.CharField(max_length=30, blank=False)
    nombre = models.CharField(max_length=60, blank=False)
    extension = models.CharField(max_length=60, blank=False)
    Rol = models.CharField(max_length=30, choices=tipo_ref,default=('', ''), blank=False)
    email = models.CharField(max_length=1000, default='', blank=False)
    password = models.CharField(max_length=255, blank=False)
    
    def save(self, *args, **kwargs):
        if self.Rol == 'Admin' or self.Rol == 'IT':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
