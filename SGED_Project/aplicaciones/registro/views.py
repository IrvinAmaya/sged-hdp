from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacultadForm, DiscapacidadForm
from .models import Facultad, Discapacidad

# Create your views here.

def funcion_index(request):
    return render(request, 'index.html')

def funcion_login(request):
    return render(request, 'login.html')

def registro_facultad(request):
    form = FacultadForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Listar-Facultades')

    contexto = {'form':form}
    return render(request, 'registrarFacultad.html', contexto)

def listar_facultades(request):
    contexto = {'lista_facultades': Facultad.objects.all().order_by('nombre_facultad')
                }
    return render(request, 'listadoFacultades.html', contexto)

def eliminar_facultad(request, id_facultad):
    facultad = get_object_or_404(Facultad, id_facultad = id_facultad)
    facultad.delete()
    return redirect('Listar-Facultades')

def modificar_facultad(request, id_facultad):
    facultad = get_object_or_404(Facultad, id_facultad = id_facultad)
    form = FacultadForm(instance=facultad)

    if request.method == 'POST':
        form = FacultadForm(request.POST, instance=facultad)
        if form.is_valid():
            form.save()
            return redirect('Listar-Facultades')

    contexto = {'form':form}
    return render(request, 'modificarFacultad.html', contexto)