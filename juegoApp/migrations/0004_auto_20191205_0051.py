# Generated by Django 2.2.4 on 2019-12-05 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juegoApp', '0003_auto_20191205_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuesta', to='juegoApp.Autores'),
        ),
    ]
