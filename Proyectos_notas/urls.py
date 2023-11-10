"""Proyectos_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postres import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('profesores/',views.profesor, name='profesor'),
    path('notas/', views.guardar_nota, name='guardar_nota'),
    path('notasapo/',views.notasap, name='notasapo'),
    path('anotaciones/', views.anotaciones_form1, name='guardar_anotacion'),
    path('anotacionesapo/',views.anotaciones_form, name='anotacionesapode'),
    path('actividadesp/',views.subir_archivo,name='subir_archivo'),
    path('actividadesalumno/',views.gestionar_archivos, name='actividades'),
    path('actividadapoderado/',views.gestionar_archivos2, name='actividades1'),

    path('alumno/',views.alumno,name='alumno'),
    path('notasal/',views.obtener_notas,name='notasal'),
    path('loginalumno/',views.logina,name="loginalu"),
    path('loginprofesor/',views.loginp,name='loginprofesor'),
    path('loginapoderado/',views.loginap,name='loginapoderado'),
    path('apoderados/',views.apoderados,name='apoderados'),
    path('registrarapo/',views.register_profesor, name='registrarapo'),
    path('registroalumno/',views.register_student, name='registroalumno'),
    path('registroprofesor/',views.register_profesor2, name='registroprofesor'),
    path('index2/',views.mostrar_datos, name='idenx1'),
    path('registro/',views.register, name='registro'),
    path('perfil/', views.get_all_user_data, name='all_users'),
    path('cargar_asignaturas/', views.listar_materias, name='cargar_asignaturas'),
    path('subir-archivo/', views.upload_file, name='upload_file'),
    path('notasedit/', views.notasedit, name='notasedit'),

]
   
 
