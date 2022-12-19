from django.db import models

# Create your models here.

class Institucion(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name="nombre de la institucion", unique=True
    )
    
    # Creamos un metodo de clase para obtener el id de la institucion por defecto en caso de que no haya ninguna disponible en el modelo
    @classmethod
    def get_default_institucion(cls):
        institucion,crear = cls.objects.get_or_create(nombre='Sin institucion disponible',defaults={'nombre':'Sin institucion disponible'},)
        
        return institucion.pk

    def __str__(self):
        return self.nombre


class Inscrito(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_inscripcion = models.DateField(auto_now_add=True)    
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, default=Institucion.get_default_institucion)
    hora = models.TimeField()
    ESTADO_CHOICES = (
        ("Reservado", "Reservado"),
        ("Completada", "Completada"),
        ("Anulada", "Anulada"),
        ("No Asisten", "No Asisten"),
    )
    estado = models.CharField(
        max_length=50, choices=ESTADO_CHOICES, default="Reservado"
    )
    observaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.nombre)