from django.contrib import admin
from .models import Curso, Entregable, Profesor, Estudiante

# Register your models here.

admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Profesor)
admin.site.register(Estudiante)