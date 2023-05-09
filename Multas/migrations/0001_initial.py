# Generated by Django 4.1.3 on 2023-05-08 22:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agencias', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multa_id', models.CharField(default=uuid.uuid4, max_length=200, unique=True)),
                ('total', models.CharField(max_length=60)),
                ('infraccion', models.CharField(choices=[('No Cumplir con los requisítos de forma', 'No Cumplir con los requisítos de forma'), ('Entrega tardía de los informes mensuales', 'Entrega tardía de los informes mensuales'), ('Uso de métodos no reconocidos por la ley 73-2019', 'Uso de métodos no reconocidos por la ley 73-2019'), ('No someter plan correctivo en 15 días', 'No someter plan correctivo en 15 días'), ('Otros, según identificado por el Director de la OIE', 'Otros, según identificado por el Director de la OIE'), ('Incumplir con las cuantías establecidas por métodos', 'Incumplir con las cuantías establecidas por métodos'), ('No cumplir con disposiciones federales', 'No cumplir con disposiciones federales'), ('Falta de referido de incumplimiento de los licitdores', 'Falta de referido de incumplimiento de los licitdores'), ('No cumplir con la entrega de contestación de requerimiento de notificación o citación', 'No cumplir con la entrega de contestación de requerimiento de notificación o citación'), ('Comprador no autorizado', 'Comprador no autorizado'), ('Falta de justificación en compras excepcionales', 'Falta de justificación en compras excepcionales'), ('No mantener actualizado la información en los registros', 'No mantener actualizado la información en los registros'), ('Primera violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019', 'Primera violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019'), ('Falta firmas no autorizadas', 'Falta firmas no autorizadas'), ('Fraccionamiento de compras', 'Fraccionamiento de compras'), ('Cifra usada no concuerda con el objeto', 'Cifra usada no concuerda con el objeto'), ('Tercera violación en Categoría I (aplicará la Primera Multa)', 'Tercera violación en Categoría I (aplicará la Primera Multa)'), ('Segunda Violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019', 'Segunda Violación con cualquier orden, resolución o decisión emitida por el Administrador según lo dispuesto en el inciso (b) de la Ley 73-2019'), ('Realizar actividades exclusivas de la SG. Art 15', 'Realizar actividades exclusivas de la SG. Art 15'), ('Incumplimienot de contrato por parte del licitador', 'Incumplimienot de contrato por parte del licitador'), ('Alteración de documentos', 'Alteración de documentos'), ('Sea convicto o se declare culpable de la comisión de delito', 'Sea convicto o se declare culpable de la comisión de delito'), ('Exclusión del RUL', 'Exclusión del RUL'), ('Tercera Violación en Categoría II (aplicará la Primera Multa)', 'Tercera Violación en Categoría II (aplicará la Primera Multa)')], max_length=200)),
                ('pago', models.BooleanField(default='True')),
                ('nombre_agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencias.agencia')),
            ],
        ),
    ]