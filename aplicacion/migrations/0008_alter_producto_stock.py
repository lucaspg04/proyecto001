# Generated by Django 4.2.1 on 2023-07-04 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_producto_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
