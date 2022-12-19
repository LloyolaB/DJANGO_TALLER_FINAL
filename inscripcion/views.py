from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormInscripcion, FormActualizarInscripcion
from django.urls import reverse_lazy
from .models import Inscrito,Institucion

# Create your views here.

def index(request):
    return render(request, "index.html")

def crear_inscripcion(request):    
    if request.method == "POST":
        form = FormInscripcion(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Inscripción creada con éxito")
            return redirect("lista_inscripcion")
        else:
            messages.warning(request, "No pudimos guardar la inscripción")
    else:
        form = FormInscripcion()
        
    return render(request, "crear_inscripcion.html", {"form": form})





def listar_inscripcion(request):
    inscrito = Inscrito.objects.all()
    data = {"inscrito": inscrito}
    return render(request, "listar_inscripcion.html", data)


def editar_inscripcion(request, id):
    queryset = Inscrito.objects.get(id=id)
    form = FormActualizarInscripcion(instance=queryset)
    if request.method == "POST":
        form = FormActualizarInscripcion(request.POST, instance=queryset)
        
        if form.is_valid():
            form.save()
        return listar_inscripcion(request)
    data = {"form": form}
    return render(request, "edit_inscripcion.html", data)


def eliminar_inscripcion(request, id):
    inscrito = Inscrito.objects.get(id=id)
    messages.success(request, f"Inscripcion {inscrito} eliminada con exito")
    inscrito.delete()
    return listar_inscripcion(request)