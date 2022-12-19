from django.shortcuts import render
from django.http import JsonResponse
from .serializers import InscritoSerializer, InstitucionSerializer
from inscripcion.models import Inscrito, Institucion
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

def institucionesJsonResponse(request):
    inscritos = Inscrito.objects.all()
    data = {'inscritos': list(inscritos.values('id', 'nombre','telefono','fecha_inscripcion','institucion','hora','estado','observaciones'))}
    return JsonResponse(data, safe=False)


@api_view(['GET', 'POST'])
def listar_instituciones(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serial = InstitucionSerializer(instituciones, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid() :
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, pk):
    try:
        institucion = Institucion.objects.get(pk=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ListaInscritos(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serial = InscritoSerializer(inscritos, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscrito(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(id=pk)
        except Inscrito.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serial = InscritoSerializer(inscrito)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritoSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    