from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

#Create your views here

def probandoTemplates(request):
    template = loader.get_template('template1.html')
    context = {}  # Puedes agregar datos al contexto si es necesario
    documento = template.render(context)
    return HttpResponse(documento)