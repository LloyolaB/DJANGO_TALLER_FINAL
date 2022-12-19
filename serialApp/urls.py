
from django.urls import path
from .views import *
urlpatterns = [
    path("instituciones", listar_instituciones, name="listar_instituciones_api"),
    path("instituciones/<int:pk>", institucion_detalle, name="institucion_detalle_api"),
    path("instituciones-api", institucionesJsonResponse, name="inscritos_json_api"),
    path("inscritos", ListaInscritos.as_view(), name="inscritos_api"),
    path("inscritos/<int:pk>", DetalleInscrito.as_view(), name="detalle_inscrito_api"),
]
    
    