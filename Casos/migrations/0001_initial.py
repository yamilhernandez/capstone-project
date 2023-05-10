# Generated by Django 4.1.3 on 2023-05-09 19:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Agencias', '0003_alter_agencia_acronimo_alter_agencia_alerta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caso_id', models.CharField(default=uuid.uuid4, max_length=200, unique=True)),
                ('id_caso', models.CharField(max_length=500, unique=True)),
                ('estado', models.CharField(choices=[('En Espera', 'En Espera'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado')], default=('', ''), max_length=30)),
                ('estatus', models.BooleanField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('nombre_agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencias.agencia')),
            ],
        ),
    ]
