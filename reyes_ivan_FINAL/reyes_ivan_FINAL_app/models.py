from django.db import models

# Create your models here.

class Estudiante(models.Model):

    ESTADO_ELECCIONES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=9)
    fechaInscripcion = models.DateField()
    institucion = models.CharField(max_length=20)
    horaInscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_ELECCIONES)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.institucion} - {self.fechaInscripcion}"
