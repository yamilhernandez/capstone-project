# Generated by Django 4.1.3 on 2023-05-15 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_reporte',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
