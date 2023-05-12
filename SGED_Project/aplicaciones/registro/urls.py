from django.urls import path
from . import views

urlpatterns = [
    path('',views.funcion_index),

    path('Listar-Facultades/Registro-Facultad/',views.registro_facultad),
    path('Listar-Facultades/',views.listar_facultades, name='Listar-Facultades'),
    path('login/',views.funcion_login),
    path('Listar-Facultades/Modificar-Facultad/<id_facultad>/',views.modificar_facultad),
    path('eliminar-facultad/<id_facultad>/',views.eliminar_facultad),
    #path('empleados/persona/',views.persona),
    #path('empleados/calculadora/',views.calc),
    #path('empleados/notas/',views.notas),

]