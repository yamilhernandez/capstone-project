# Generated by Django 4.1.3 on 2023-05-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompraSometida', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprasometida',
            name='fondos',
            field=models.CharField(choices=[('Estatal', 'Estatal'), ('Federal', 'Federal')], default=('', ''), max_length=1000),
        ),
        migrations.AlterField(
            model_name='comprasometida',
            name='procedencia',
            field=models.CharField(choices=[('PR', 'PR'), ('USA', 'USA'), ('EXT', 'EXT')], default=('', ''), max_length=1000),
        ),
    ]
