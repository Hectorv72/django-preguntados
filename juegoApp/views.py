from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
#from .forms import FormCargarCat
from .forms import *
from .models import *
import random
# Create your views here.

def home(request):
    if request.method == "POST":
        nom = request.POST['validador']
        form = Jugador(request.POST)
        valid = False

        bd = Jugadores.objects.all()
        for i in bd:
            if nom == i.nombre:
                valid = True

        if form.is_valid() and valid == False:
            form.save()

    return render(request,'juegoApp/home.html')

def Selector(request):
    return render(request,'juegoApp/home.html')

def Juego(request):
    if request.method == "POST":
        permitir = 0
        id = request.POST['rul']
        if id != '999':
            bd = Preguntas.objects.all().filter(categoria = id)
        else:
            bd = Preguntas.objects.all()

        for i in bd:
            permitir += 1

        if permitir > 0:
            PreguntaElegida = random.choice(bd)
            ide = PreguntaElegida.id
            respuesta = PreguntaElegida.respuesta
            tabla = []
            opciones = []
            tabla.append(PreguntaElegida.respuesta)
            tabla.append(PreguntaElegida.opcion1)
            tabla.append(PreguntaElegida.opcion2)
            tabla.append(PreguntaElegida.opcion3)
            for i in range(4):
                num = random.choice(tabla)
                opciones.append(num)
                tabla.remove(num)
            return render(request,'juegoApp/juego.html',{'Pregunta':PreguntaElegida,'Opciones':opciones,'Respuesta':respuesta,'Ide':ide})
        else:
            val = "No hay preguntas en esta categoria"
            return render(request,'juegoApp/error.html',{"Respuesta":val})
    else:
        val = "Ah ocurrido un error vuelve a atras"
        return render(request,'juegoApp/error.html',{"Respuesta":val})


def Ruleta(request):

    bd = Categorias.objects.all()
    categorias = []
    tabla = []
    cantidad = 0
    for i in bd:
        tabla.append(i)
        cantidad += 1
    
    for i in bd:
        selector = random.choice(tabla)
        categorias.append(selector)
        tabla.remove(selector)

    return render(request,'juegoApp/ruleta.html',{'Categorias':categorias,
    'Cantidad':cantidad,
    })


def Informacion(request):
    if request.method == "POST":
        id = request.POST['Pregunta']
        bd = Preguntas.objects.all().filter(id = id)
        elegido = random.choice(bd)

    return render(request,'juegoApp/informacion.html',{'Pregunta':elegido})

def Perder(request):
    if request.method == "POST":
        id = request.POST['Pregunta']
        bd = Preguntas.objects.all().filter(id = id)
        elegido = random.choice(bd)

        bdJugadores = Jugadores.objects.all()
        jugadores = []
        form = Jugador()

        for i in bdJugadores:
            jugadores.append(i.nombre)

    return render(request,'juegoApp/perder.html',{'Pregunta':elegido,'Jugadores':jugadores,'Formulario':form})

def Score(request):
    bd = Jugadores.objects.all()

    return render(request,'juegoApp/puntajes.html',{'Datos':bd})


#-------------------------------------------comentarios-----------------------------------------------------

def prueba(request):
    id_com = ''
    
    if request.GET.get('r'):
        id_com = request.GET['r']
        id_com = int(id_com)

    if request.method == 'POST':
        formCom = FormComentario(request.POST)
        formCom.save()
    formCom = FormComentario()
    comentarios = Comentarios.objects.all()
    
    
    return render(request,'juegoApp/mandar.html',{'FormComentario':formCom,
    'Comentarios':comentarios,
    'idComentario': id_com,
    })

def elimcom(request):
    if request.method == 'POST':
        elim = request.POST['com']
        bd = Comentarios.objects.get(id = elim)
        for i in Comentarios.objects.filter(respuesta=elim):
            i.delete()
        bd.delete()
    return redirect('prueba')