from django import forms
from django.forms import inlineformset_factory
from .models import Facultad, Discapacidad

class DiscapacidadForm(forms.ModelForm):
    class Meta:
        model = Discapacidad
        exclude = ['id_discapacidad']
        fields = ['tipo_discapacidad', 'cantidad_discapacitados']
        labels = {
            'tipo_discapacidad': 'Tipo de discapacidad',
            'cantidad_discapacitados': 'Cantidad de estudiantes discapacitados',
        }


class FacultadForm(forms.ModelForm):
    discapacidades = forms.inlineformset_factory(Facultad, Discapacidad, form=DiscapacidadForm, extra=1)

    class Meta:
        model = Facultad
        exclude = ['id_facultad']
        fields = ['nombre_facultad', 'cantidad_estudiantes', 'nombre_universidad', 'anio_informacion']
        labels = {
            'nombre_facultad': 'Nombre de la facultad',
            'cantidad_estudiantes': 'Cantidad de estudiantes',
            'nombre_universidad': 'Nombre de la universidad',
            'anio_informacion': 'Año de la información',
        }


DiscapacidadFormSet = inlineformset_factory(Facultad, Discapacidad,fields=("tipo_discapacidad","cantidad_discapacitados"), form=DiscapacidadForm, extra=10, fk_name='facultad')

