# Generated by Django 4.2.1 on 2023-07-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='aplicacion.marca'),
        ),
    ]
