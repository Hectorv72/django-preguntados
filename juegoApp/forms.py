from django.forms import ModelForm
from django import forms
from .models import *
#from . import models

class Jugador(ModelForm):
	class Meta:
		model = Jugadores
		fields = ['nombre','puntaje']
		widgets = {'nombre': forms.HiddenInput(),'puntaje': forms.HiddenInput(),}


class FormComentario(ModelForm):
	class Meta:
		model = Comentarios
		fields = ['autor','comentario','respuesta']