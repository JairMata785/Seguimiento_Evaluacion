from django.core.management.base import BaseCommand
from evaluaciones.models import Docente, Semestre, Evaluacion
from datetime import date

class Command(BaseCommand):
    help = 'Loads test data into the database'

    def handle(self, *args, **kwargs):
        # Create test docentes for Informática
        docentes_inf = [
            Docente.objects.create(
                nombre="Juan",
                apellidos="Pérez García",
                email="juan.perez@universidad.edu",
                departamento="Matemáticas",
                carrera="INF"
            ),
            Docente.objects.create(
                nombre="María",
                apellidos="López Sánchez",
                email="maria.lopez@universidad.edu",
                departamento="Programación",
                carrera="INF"
            ),
        ]

        # Create test docentes for Sistemas Computacionales
        docentes_isc = [
            Docente.objects.create(
                nombre="Carlos",
                apellidos="Ramírez Torres",
                email="carlos.ramirez@universidad.edu",
                departamento="Redes",
                carrera="ISC"
            ),
            Docente.objects.create(
                nombre="Ana",
                apellidos="Martínez Ruiz",
                email="ana.martinez@universidad.edu",
                departamento="Base de Datos",
                carrera="ISC"
            ),
        ]

        # Create test semestres
        semestres = [
            Semestre.objects.create(
                nombre="2024-1",
                fecha_inicio=date(2024, 1, 15),
                fecha_fin=date(2024, 6, 30)
            ),
            Semestre.objects.create(
                nombre="2024-2",
                fecha_inicio=date(2024, 7, 15),
                fecha_fin=date(2024, 12, 15)
            ),
        ]

        # Create test evaluaciones with different scores
        for docente in docentes_inf + docentes_isc:
            for semestre in semestres:
                Evaluacion.objects.create(
                    docente=docente,
                    semestre=semestre,
                    puntaje_general=4.5 if docente.carrera == 'INF' else 4.7,
                    comentarios=f"Excelente desempeño en el semestre - {docente.get_carrera_display()}"
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded test data'))