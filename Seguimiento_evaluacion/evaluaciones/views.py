from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Docente, Evaluacion, Semestre
from django.urls import reverse_lazy
from django.db.models import Avg
from django.db.models.functions import TruncMonth

class DocenteListView(ListView):
    model = Docente
    template_name = 'evaluaciones/docente_list.html'
    context_object_name = 'docentes'

from django.views.generic import ListView
from .models import Evaluacion, Docente, Semestre

class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_list.html'
    context_object_name = 'evaluaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docentes'] = Docente.objects.all()
        context['semestres'] = Semestre.objects.all()
        return context

def dashboard(request):
    context = {
        'total_docentes': Docente.objects.count(),
        'total_docentes_inf': Docente.objects.filter(carrera='INF').count(),
        'total_docentes_isc': Docente.objects.filter(carrera='ISC').count(),
        'promedio_general': Evaluacion.objects.aggregate(Avg('puntaje_general'))['puntaje_general__avg'],
        'evaluaciones': Evaluacion.objects.select_related('docente', 'semestre').order_by('-fecha_evaluacion')[:10]
    }
    
    # Get promedio por semestre
    promedios_semestre = Evaluacion.objects.values('semestre__nombre').annotate(
        promedio=Avg('puntaje_general')
    ).order_by('semestre__nombre')

    # Get distribución de evaluaciones
    distribucion_evaluaciones = {
        'Excelente': Evaluacion.objects.filter(puntaje_general__gte=4.5).count(),
        'Bueno': Evaluacion.objects.filter(puntaje_general__range=(4.0, 4.4)).count(),
        'Regular': Evaluacion.objects.filter(puntaje_general__range=(3.5, 3.9)).count(),
        'Bajo': Evaluacion.objects.filter(puntaje_general__range=(3.0, 3.4)).count(),
        'Deficiente': Evaluacion.objects.filter(puntaje_general__lt=3.0).count(),
    }

    context.update({
        'distribucion_evaluaciones': distribucion_evaluaciones,
        'promedios_semestre': promedios_semestre,  # Agregamos esto al contexto
    })
    return render(request, 'evaluaciones/dashboard.html', context)

def reportes_view(request):
    # Get average scores by month
    promedios_mensuales = Evaluacion.objects.annotate(
        mes=TruncMonth('fecha_evaluacion')
    ).values('mes').annotate(
        promedio=Avg('puntaje_general')
    ).order_by('mes')

    # Get top performing teachers
    mejores_docentes = Docente.objects.annotate(
        promedio=Avg('evaluacion__puntaje_general')
    ).order_by('-promedio')[:5]

    return render(request, 'evaluaciones/reportes.html', {
        'promedios_mensuales': promedios_mensuales,
        'mejores_docentes': mejores_docentes,
    })
