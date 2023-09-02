from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Curso, Entregable, Profesor, Estudiante



#Create your views here

def probandoTemplates(request):
    template = loader.get_template('template1.html')
    context = {}  # Puedes agregar datos al contexto si es necesario
    documento = template.render(context)
    return HttpResponse(documento)

def curso_list(request):
    curso = Curso.objects.all()
    return render(request, "curso_list.html", {"curso": curso})

def curso_create(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        numero_comision = request.POST.get("numero_comision")
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect("curso_list")
    
    return render(request, "curso_create.html")

def index(request):
        return render(request, "index.html")

def entregables_list(request):
     entregables = Entregable.objects.all()
     return render(request, "entregables_list.html", {"entregables": entregables})

def profesor_list(request):
     profesores = Profesor.objects.all()
     return render(request, "profesor_list.html", {"profesores": profesores})

def estudiantes_list(request):
     estudiantes = Estudiante.objects.all()
     return render(request, "estudiantes_list.html", {"estudiantes": estudiantes})