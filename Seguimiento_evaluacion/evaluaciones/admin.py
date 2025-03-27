from django.contrib import admin
from .models import Docente, Semestre, Evaluacion

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'departamento')
    search_fields = ('nombre', 'apellidos', 'email')

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('docente', 'semestre', 'puntaje_general', 'fecha_evaluacion')
    list_filter = ('semestre', 'docente')
