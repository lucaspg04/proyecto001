# Generated by Django 4.2.1 on 2023-07-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_categoria_alter_marca_id_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
