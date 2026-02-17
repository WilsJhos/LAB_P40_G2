from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    PRIORIDADES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    estado = models.CharField(max_length=15, choices=ESTADOS, default='pendiente')
    
    class Meta:
        ordering = ['-prioridad', 'fecha_vencimiento']
    
    def __str__(self):
        return self.titulo
    
    def marcar_completada(self):
        self.estado = 'completada'
        self.fecha_completada = timezone.now()
        self.save()
    
    def dias_restantes(self):
        if self.fecha_vencimiento:
            delta = self.fecha_vencimiento - timezone.now()
            return delta.days
        return None