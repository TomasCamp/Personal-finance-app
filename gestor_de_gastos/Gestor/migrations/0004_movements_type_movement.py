# Generated by Django 5.1.5 on 2025-01-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0003_alter_movements_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movements',
            name='type_movement',
            field=models.BooleanField(default=False, verbose_name='Tipo de Movimiento'),
        ),
    ]
