# Generated by Django 4.2.1 on 2023-07-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_pedido_monto_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('GO', 'Gorro'), ('PO', 'Polera'), ('PL', 'Poleron'), ('CH', 'Chaqueta'), ('LE', 'Lentes')], max_length=2, null=True),
        ),
    ]