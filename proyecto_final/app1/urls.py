from django.urls import path
from . import views

app_name = 'app1'  # Si estás usando namespaces, define el nombre de la aplicación

urlpatterns = [
    path('probandoTemplate/', views.probandoTemplates, name="Probando Template"), 
    path('curso_list/', views.curso_list, name="curso_list"), 
    path('curso_create/', views.curso_create, name="curso_create"), 
    path('index/', views.index, name="index"), 
    path('entregables_list/', views.entregables_list, name="entregables_list"), 
    path('profesor_list/', views.profesor_list, name="profesor_list"), 


]