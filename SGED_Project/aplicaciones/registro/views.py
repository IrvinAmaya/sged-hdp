from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacultadForm, DiscapacidadForm, DiscapacidadFormSet
from .models import Facultad, Discapacidad
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from random import randrange
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def funcion_index(request):
    return render(request, 'index.html')

def funcion_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña es incorrecto'
                })
        else:
            login(request,user)
            return redirect('Listar-Facultades')

@login_required
def funcion_logout(request):
    logout(request)
    return redirect ('/')

@login_required
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

@login_required
def listar_facultades(request):
    contexto = {'lista_facultades': Facultad.objects.all().order_by('nombre_facultad')
                }
    return render(request, 'listadoFacultades.html', contexto)

@login_required
def eliminar_facultad(request, id_facultad):
    facultad = get_object_or_404(Facultad, id_facultad = id_facultad)
    facultad.delete()
    return redirect('Listar-Facultades')

@login_required
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



#Graficas
def datos(request):
    contexto = {'lista_facultades': Facultad.objects.all().order_by('nombre_facultad'),
                'discapacidades': Discapacidad.objects.all(),
                }
    return render(request, 'datos.html', contexto)

def graficas(request):

    return render(request, 'graficas.html')

def fuentes(request):

    return render(request, 'fuentes.html')

def get_chart(_request):

    facultades = Facultad.objects.all()
    nombres_facultades = []
    estudiantes_facultades = []

    for f in facultades:
        nombres_facultades.append(f.nombre_facultad)
        estudiantes_facultades.append(f.cantidad_estudiantes)


    chart = {
        'title':{
            'text':"Facultades"
        },
        'tooltip': {
            'show': True,
            'trigger': "axis",
            'triggerOn': "mousemove|click",
            'axisPointer': {
                'type': "cross",
                'label': {
                'backgroundColor': "#6a7985"
                }
            }
        },
        'xAxis': [
            {
                'type': "category",
                'boundaryGap': "false",
                'data': nombres_facultades
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [
            {
                'data': estudiantes_facultades,
                'type': "line",
                'itemStyle': {
                    'color': 'red'
                },
                'lineStyle': {
                    'color': 'blue'
                }
            }
        ]
    }

    return JsonResponse(chart)

def get_chart2(_request):

    facultades = Facultad.objects.all()
    discapacidades = Discapacidad.objects.all()
    tipos_discapacidades = []
    cantidades_discapacidades = []
    nombres_facultades = []
    estudiantes_facultades = []
    nombres_universidades = []

    for d in discapacidades:
        tipos_discapacidades.append(d.tipo_discapacidad)
        cantidades_discapacidades.append(d.cantidad_discapacitados)

    for f in facultades:
        nombres_facultades.append(f.nombre_facultad)
        estudiantes_facultades.append(f.cantidad_estudiantes)
        nombres_universidades.append(f.nombre_universidad)
        


    chart2 = {
        'title':{
            'text':"Universidades"
        },
        'tooltip': {
            'show': True,
            'trigger': "axis",
            'triggerOn': "mousemove|click",
            'axisPointer': {
                'type': "shadow",
                'label': {
                'backgroundColor': "#6a7985"
                }
            }
        },
         'toolbox': {
        'show': "true",
        'orient': "vertical",
        'left': "right",
        'top': "center",
        'feature': {
        'mark': { 'show': "true" },
        'dataView': { 'show': True, 'readOnly': False },
        'magicType': { 'show': True, 'type': ["line", "bar", "stack"] },
        'restore': { 'show': True },
        'saveAsImage': { 'show': True }
        }
        },
        'xAxis': [
            {
                'type': "category",
                'axisTick': "false",
                'data': nombres_universidades
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [
            
            {
                'data': cantidades_discapacidades,
                'type': "bar",
                'barGap':"0",
                'label': "labelOption",
                'emphasis': {
                    'focus': 'series'
                },
                
            },
            
        ]
    }

    return JsonResponse(chart2)