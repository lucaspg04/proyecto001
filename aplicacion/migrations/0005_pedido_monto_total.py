# Generated by Django 4.2.1 on 2023-07-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_pedido_detallepedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='monto_total',
            field=models.FloatField(null=True),
        ),
    ]
