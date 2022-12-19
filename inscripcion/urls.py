from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("crear-inscripcion/", crear_inscripcion, name="crear_inscripcion"),
    path("listar-inscripcion/", listar_inscripcion, name="lista_inscripcion"),
    path("editar-inscripcion/<int:id>", editar_inscripcion, name="editar_inscripcion"),
    path("eliminar-inscripcion/<int:id>", eliminar_inscripcion, name="eliminar_inscripcion"),
]
