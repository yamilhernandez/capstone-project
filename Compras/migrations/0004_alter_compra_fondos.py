# Generated by Django 4.1.3 on 2023-05-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0003_alter_compra_num_licitador_alter_compra_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fondos',
            field=models.CharField(choices=[('Estatal', 'Estatal'), ('Federal', 'Federal')], default=('', ''), max_length=1000),
        ),
    ]