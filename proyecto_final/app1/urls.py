from django.urls import path
from . import views

urlspatterns = [
    path('probandoTemplate/', views.probandoTemplates, name = "Probando Template"), 
]