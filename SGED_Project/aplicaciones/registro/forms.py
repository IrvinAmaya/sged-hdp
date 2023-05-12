from django import forms
from .models import Facultad, Discapacidad

class FacultadForm(forms.ModelForm):

    class Meta:
        model = Facultad
        #fields = '__all__' para mostrar todos los campos

        fields = [
            'nombre_facultad',
            'cantidad_estudiantes',
            'nombre_universidad',
            'anio_informacion',
            
        ] #Para elegir que campos se desea mostrar

class DiscapacidadForm(forms.ModelForm):

    class Meta:
        model = Discapacidad
        #fields = '__all__' para mostrar todos los campos

        fields = [
            'tipo_discapacidad',
            'cantidad_discapacitados',            
        ] #Para elegir que campos se desea mostrar