from django.db import models
from django import forms

# Create your models here.
def subir_iconos(instance, filename):
	return 'iconos/%s'% filename

def subir_imagenes(instance, filename):
	return 'imagenes/%s'% filename

class Categorias(models.Model):
    nombre = models.CharField(max_length=30)
    icono = models.ImageField(upload_to=subir_iconos,blank=True,null=True)
    color = models.CharField(max_length=7,null=True)
    
    def __str__(self):
        return self.nombre


class Niveles(models.Model):
    dificultad = models.CharField(max_length=30)
    
    def __str__(self):
        return self.dificultad

class Jugadores(models.Model):
    nombre = models.CharField(max_length=20)
    puntaje = models.IntegerField(max_length=3,null=True)
    #nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nombre

class Preguntas(models.Model):
    pregunta = models.TextField (max_length=300)
    imagen = models.ImageField(upload_to=subir_imagenes, blank=True)
    respuesta = models.TextField (max_length=150)
    opcion1 = models.TextField (max_length=150)
    opcion2 = models.TextField (max_length=150)
    opcion3 = models.TextField (max_length=150)
    informacion = models.TextField(max_length=700,null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE,blank=True, null=True)
    #nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE, null=True)

    IMAGEN_OPTIONS = (
	(1,'Si'),
	(2,'No'),
	)
    conimagen = models.IntegerField(choices=IMAGEN_OPTIONS, default=IMAGEN_OPTIONS[1],null=True)
    
    def __str__(self):
        return self.pregunta


#------------------------------------------------------------

class Autores(models.Model):
    nom_autor = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_autor

class Comentarios(models.Model):
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE,null=False,related_name='autor')
    comentario = models.TextField(max_length=300,null=False)
    respuesta = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.comentario