# Generated by Django 2.2.4 on 2019-12-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegoApp', '0005_auto_20191205_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='respuesta',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]
