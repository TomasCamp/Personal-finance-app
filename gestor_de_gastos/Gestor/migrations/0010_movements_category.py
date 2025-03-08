# Generated by Django 5.1.5 on 2025-03-02 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor', '0009_categories_type_movement'),
    ]

    operations = [
        migrations.AddField(
            model_name='movements',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='Gestor.categories'),
            preserve_default=False,
        ),
    ]
