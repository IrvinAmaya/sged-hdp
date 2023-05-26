from django.urls import path
from . import views


urlpatterns = [
    path('',views.funcion_index),
    path('fuentes', views.fuentes, name='fuentes'),
    path('graficas', views.graficas, name='graficas'),
    path('datos', views.datos, name='datos'),
    path('Listar-Facultades/Registro-Facultad/',views.registro_facultad),
    path('Listar-Facultades/Modificar-Facultad/<id_facultad>/',views.modificar_facultad),
    path('Listar-Facultades/',views.listar_facultades, name='Listar-Facultades'),
    path('login/',views.funcion_login, name='login'),
    path('logout/',views.funcion_logout, name='logout'),
    path('eliminar-facultad/<id_facultad>/',views.eliminar_facultad),
    path('get_chart/', views.get_chart, name='get_chart'),
    path('get_chart2/', views.get_chart2, name='get_chart2'),
]