import uuid

from django.db import models

from django.db import models
from django.template.defaultfilters import default
from django.utils import timezone


class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    licencia_conducir = models.CharField(max_length=50, unique=True)
    dni = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - Licencia: {self.licencia_conducir}"


class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    anio = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo} ({self.anio})"


class ConductorVehiculo(models.Model):
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(default=timezone.now)
    fecha_fin_asignacion = models.DateField(null=True, blank=True)
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.conductor} - {self.vehiculo} desde {self.fecha_asignacion}"


class RevisionTecnica(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='revisiones_tecnicas')
    fecha_revision = models.DateField()
    resultado = models.CharField(max_length=100)
    observaciones = models.CharField("Observaciones", blank=True, null=True, max_length=150)

    class Meta:
        unique_together = (('vehiculo'),)

    def __str__(self):
        return f"Revision {self.fecha_revision} - {self.vehiculo}"


class Infraccion(models.Model):
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name='infracciones')
    fecha_infraccion = models.DateField()
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Infracción {self.fecha_infraccion} - {self.conductor}"


class Incidencia(models.Model):
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name='incidencias')
    fecha_incidencia = models.DateField(default=timezone.now)
    descripcion = models.CharField("Descripcion", max_length=150, blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=[
        ('Queja', 'Queja de Servicio'),
        ('Accidente', 'Accidente'),
        ('Otro', 'Otro tipo de incidencia')
    ])

    def __str__(self):
        return f"Incidencia {self.tipo} - {self.conductor} en {self.fecha_incidencia}"


class ExcesoVelocidad(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='excesos_velocidad')
    fecha_evento = models.DateTimeField(default=timezone.now)
    velocidad = models.DecimalField(max_digits=5, decimal_places=2)
    ubicacion = models.CharField(max_length=200)  # O un campo JSONField para almacenar coordenadas

    def __str__(self):
        return f"Exceso de velocidad {self.velocidad} km/h - {self.vehiculo} en {self.fecha_evento}"
