from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre_facultad = models.CharField(max_length=80)
    cantidad_estudiantes = models.IntegerField(validators=[MaxValueValidator(9999999)])
    nombre_universidad = models.CharField(max_length=80)
    anio_informacion = models.IntegerField(
        validators=[MaxValueValidator(9999)],
    )
    

class Discapacidad(models.Model):
    id_discapacidad = models.AutoField(primary_key=True)
    tipo_discapacidad = models.CharField(max_length=80)
    cantidad_discapacitados = models.IntegerField(validators=[MaxValueValidator(9999999)])    
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.tipo_discapacidad + str(self.cantidad_discapacitados)