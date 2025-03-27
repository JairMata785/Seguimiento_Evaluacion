from django.urls import path
from . import views

app_name = 'evaluaciones'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('docentes/', views.DocenteListView.as_view(), name='docente_list'),
    path('evaluaciones/', views.EvaluacionListView.as_view(), name='evaluacion_list'),
    path('reportes/', views.reportes_view, name='reportes'),  # Add this line
]