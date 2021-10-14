# Generated by Django 2.2.4 on 2019-12-05 03:43

from django.db import migrations, models
import django.db.models.deletion
import juegoApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_autor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('icono', models.ImageField(blank=True, null=True, upload_to=juegoApp.models.subir_iconos)),
                ('color', models.CharField(max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('puntaje', models.IntegerField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Niveles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dificultad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField(max_length=300)),
                ('imagen', models.ImageField(blank=True, upload_to=juegoApp.models.subir_imagenes)),
                ('respuesta', models.TextField(max_length=150)),
                ('opcion1', models.TextField(max_length=150)),
                ('opcion2', models.TextField(max_length=150)),
                ('opcion3', models.TextField(max_length=150)),
                ('informacion', models.TextField(max_length=700, null=True)),
                ('conimagen', models.IntegerField(choices=[(1, 'Si'), (2, 'No')], default=(2, 'No'), null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juegoApp.Categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=300)),
                ('autor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='juegoApp.Autores')),
            ],
        ),
    ]