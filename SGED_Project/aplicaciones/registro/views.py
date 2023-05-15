from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacultadForm, DiscapacidadForm, DiscapacidadFormSet
from .models import Facultad, Discapacidad
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

# Create your views here.

def funcion_index(request):
    return render(request, 'index.html')

def funcion_login(request):
    return render(request, 'login.html')

def registro_facultad(request):

    if request.method == 'POST':
        facultad_form = FacultadForm(request.POST)
        discapacidad_formset = DiscapacidadFormSet(request.POST)
        if facultad_form.is_valid() and discapacidad_formset.is_valid():
            facultad = facultad_form.save()
            discapacidad_formset.instance = facultad
            discapacidad_formset.save()
            return redirect('Listar-Facultades')
    else:
        facultad_form = FacultadForm()
        discapacidad_formset = DiscapacidadFormSet()
    return render(request, 'registrarFacultad.html', {'facultad_form': facultad_form, 'discapacidad_formset': discapacidad_formset}) 


def listar_facultades(request):
    contexto = {'lista_facultades': Facultad.objects.all().order_by('nombre_facultad')
                }
    return render(request, 'listadoFacultades.html', contexto)

def eliminar_facultad(request, id_facultad):
    facultad = get_object_or_404(Facultad, id_facultad = id_facultad)
    facultad.delete()
    return redirect('Listar-Facultades')


def modificar_facultad(request, id_facultad):
    facultad = get_object_or_404(Facultad, id_facultad=id_facultad)
    facultad_form = FacultadForm(instance=facultad)
    discapacidad_formset = DiscapacidadFormSet(instance=facultad)

    if request.method == 'POST':
        facultad_form = FacultadForm(request.POST, instance=facultad)
        discapacidad_formset = DiscapacidadFormSet(request.POST, instance=facultad)
        if facultad_form.is_valid() and discapacidad_formset.is_valid():
            facultad_form.save()
            discapacidad_formset.save()
            return redirect('Listar-Facultades')

    contexto = {
        'facultad_form': facultad_form,
        'discapacidad_formset': discapacidad_formset
    }
    return render(request, 'modificarFacultad.html', contexto)



