from rest_framework import serializers
from inscripcion.models import Inscrito, Institucion

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"

class InscritoSerializer(serializers.ModelSerializer):
    institucion = InstitucionSerializer()
    class Meta:
        model = Inscrito
        fields = "__all__"
        
        