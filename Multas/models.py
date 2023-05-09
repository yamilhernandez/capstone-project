from django.db import models
#from Casos.models import Caso
from Agencias.models import Agencia
# Create your models here.
import uuid

#from datetime import datetime
# Create your models here.
tipo_infraccion = (('No Cumplir con los requisítos de forma', 'No Cumplir con los requisítos de forma'), ('Entrega tardía de los informes mensuales', 'Entrega tardía de los informes mensuales'), ('Uso de métodos no reconocidos por la ley 73-2019', 'Uso de métodos no reconocidos por la ley 73-2019'),
                   ('No someter plan correctivo en 15 días', 'No someter plan correctivo en 15 días'), ('Otros, según identificado por el Director de la OIE', 'Otros, según identificado por el Director de la OIE'), (
                       'Incumplir con las cuantías establecidas por métodos', 'Incumplir con las cuantías establecidas por métodos'),
                   ('No cumplir con disposiciones federales', 'No cumplir con disposiciones federales'), ('Falta de referido de incumplimiento de los licitdores', 'Falta de referido de incumplimiento de los licitdores'), (
                       'No cumplir con la entrega de contestación de requerimiento de notificación o citación', 'No cumplir con la entrega de contestación de requerimiento de notificación o citación'),
                   ('Comprador no autorizado', 'Comprador no autorizado'), ('Falta de justificación en compras excepcionales', 'Falta de justificación en compras excepcionales'), (
                       'No mantener actualizado la información en los registros', 'No mantener actualizado la información en los registros'),
                   ('Primera violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019',
                    'Primera violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019'),
                   ('Falta firmas no autorizadas', 'Falta firmas no autorizadas'), ('Fraccionamiento de compras', 'Fraccionamiento de compras'), (
                       'Cifra usada no concuerda con el objeto', 'Cifra usada no concuerda con el objeto'), ('Tercera violación en Categoría I (aplicará la Primera Multa)', 'Tercera violación en Categoría I (aplicará la Primera Multa)'),
                   ('Segunda Violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019',
                    'Segunda Violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019'),
                   ('Realizar actividades exclusivas de la SG. Art 15', 'Realizar actividades exclusivas de la SG. Art 15'), ('Incumplimienot de contrato por parte del licitador', 'Incumplimienot de contrato por parte del licitador'), (
                       'Alteración de documentos', 'Alteración de documentos'), ('Sea convicto o se declare culpable de la comisión de delito', 'Sea convicto o se declare culpable de la comisión de delito'),
                   ('Exclusión del RUL', 'Exclusión del RUL'), ('Tercera Violación en Categoría II (aplicará la Primera Multa)', 'Tercera Violación en Categoría II (aplicará la Primera Multa)'))


class Multa(models.Model):
    multa_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    nombre_agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    #num_caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    total = models.CharField(max_length=60,  blank=False)
    infraccion = models.CharField(
        max_length=200, choices=tipo_infraccion, blank=False)
    pago = models.BooleanField(blank=False, default='True')
