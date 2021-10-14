from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('ruleta/',views.Ruleta,name="ruleta"),
    path('juego/',views.Juego,name="juego"),
    path('informacion/',views.Informacion,name="info"),
    path('perder/',views.Perder,name="perder"),
    path('puntajes/',views.Score,name="score"),

    path('prueba/',views.prueba,name="prueba"),
    path('eliminar/',views.elimcom,name="elimcom"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)