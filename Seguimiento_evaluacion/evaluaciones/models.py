from django.db import models

class Docente(models.Model):
    CARRERA_CHOICES = [
        ('INF', 'Ingeniería en Informática'),
        ('ISC', 'Ingeniería en Sistemas Computacionales'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()
    departamento = models.CharField(max_length=100)
    carrera = models.CharField(max_length=3, choices=CARRERA_CHOICES, default='INF')

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.get_carrera_display()}"

class Semestre(models.Model):
    nombre = models.CharField(max_length=50)  # Ejemplo: "2023-1"
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Evaluacion(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    puntaje_general = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_evaluacion = models.DateField(auto_now_add=True)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Evaluación de {self.docente} - {self.semestre}"
