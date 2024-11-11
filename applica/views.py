from tempfile import template

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView

from applica.models import RevisionTecnica


class DashboardTemplateView(TemplateView):
    template_name = 'vehicle/dashboard.html'


class ReporteVelcidadTemplateView(TemplateView):
    template_name = "vehicle/reporte_velocidad.html"


class RevisionTecnicaTemplateView(TemplateView):
    template_name = "vehicle/alerta_revision.html"

    def get_context_data(self, **kwargs):
        context = super(RevisionTecnicaTemplateView, self).get_context_data(**kwargs)

        # Obtener todas las revisiones técnicas, ordenadas por fecha desde la más antigua a la más reciente
        revisiones = RevisionTecnica.objects.all().order_by('fecha_revision')

        # Obtener la fecha actual
        fecha_actual = timezone.now().date()

        alertas = []

        for revision in revisiones:
            # Calcular el tiempo transcurrido desde la fecha de revisión
            tiempo_transcurrido = fecha_actual - revision.fecha_revision
            meses_transcurridos = tiempo_transcurrido.days / 30  # Aproximadamente 30 días por mes

            # Determinar el color de la alerta según la antigüedad
            if meses_transcurridos > 11:
                alerta_clase = 'alert alert-danger'  # Rojo: Más de 11 meses
            elif 10 <= meses_transcurridos <= 11:
                alerta_clase = 'alert alert-warning'  # Amarillo: Entre 10 y 11 meses
            else:
                alerta_clase = 'alert alert-success'  # Verde: Menos de 10 meses

            alertas.append({
                'revision': revision,
                'alerta_clase': alerta_clase,
                'meses_transcurridos': meses_transcurridos,
            })

        # Añadir la lista de alertas al contexto
        context['alertas'] = alertas
        return context
