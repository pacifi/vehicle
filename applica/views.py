from tempfile import template

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView

from applica.models import RevisionTecnica, Soat


class DashboardTemplateView(TemplateView):
    template_name = 'vehicle/dashboard.html'


class ReporteVelcidadTemplateView(TemplateView):
    template_name = "vehicle/reporte_velocidad.html"


class AlertaRevisionTecnicaTemplateView(TemplateView):
    template_name = "vehicle/alerta_revision.html"

    def get_context_data(self, **kwargs):
        context = super(AlertaRevisionTecnicaTemplateView, self).get_context_data(**kwargs)

        # Obtener todas las revisiones técnicas, ordenadas por fecha desde la más antigua a la más reciente
        revisiones = RevisionTecnica.objects.all().order_by('fecha_revision')

        # Obtener la fecha actual
        fecha_actual = timezone.now().date()

        alertas = []

        for revision in revisiones:
            # Calcular el tiempo transcurrido desde la fecha de revisión
            tiempo_transcurrido = fecha_actual - revision.fecha_revision
            meses_transcurridos = tiempo_transcurrido.days / 30  # Aproximadamente 30 días por mes
            dias_restantes = 365 - tiempo_transcurrido.days
            vencido = False  # Variable para indicar si está vencido

            if dias_restantes < 0:
                dias_restantes = abs(dias_restantes)  # Convertir a positivo para mostrar días vencidos
                vencido = True

            # Determinar el color de la alerta según los meses transcurridos
            if meses_transcurridos >= 12:
                alerta_clase = 'alert alert-danger'  # Rojo: Más de 12 meses (un año o más)
            elif 11 <= meses_transcurridos < 12:
                alerta_clase = 'alert alert-warning'  # Amarillo: Entre 11 y 12 meses (falta un mes o menos)
            else:
                alerta_clase = 'alert alert-success'  # Verde: Menos de 11 meses

            alertas.append({
                'revision': revision,
                'alerta_clase': alerta_clase,
                'meses_transcurridos': meses_transcurridos,
                'dias_restantes': dias_restantes,
                'vencido': vencido,  # Indica si está vencido
            })

        # Añadir la lista de alertas al contexto
        context['alertas'] = alertas
        return context


class ReporteIncidenciasTemplateView(TemplateView):
    template_name = "vehicle/reporte_incidencias.html"

    def get_context_data(self, **kwargs):
        context = super(ReporteIncidenciasTemplateView, self).get_context_data(**kwargs)
        return context


class AlertaSoatTemplateView(TemplateView):
    template_name = "vehicle/alerta_soat.html"

    def get_context_data(self, **kwargs):
        context = super(AlertaSoatTemplateView, self).get_context_data(**kwargs)

        # Obtener todas las revisiones del SOAT, ordenadas por fecha de renovación
        revisiones = Soat.objects.all().order_by('fecha_renovacion')

        # Obtener la fecha actual
        fecha_actual = timezone.now().date()

        alertas = []

        for revision in revisiones:
            # Calcular el tiempo transcurrido desde la fecha de renovación
            tiempo_transcurrido = fecha_actual - revision.fecha_renovacion
            meses_transcurridos = tiempo_transcurrido.days / 30  # Aproximadamente 30 días por mes
            dias_restantes = 365 - tiempo_transcurrido.days
            vencido = False  # Variable para indicar si está vencido

            if dias_restantes < 0:
                dias_restantes = abs(dias_restantes)  # Convertir a positivo para mostrar días vencidos
                vencido = True

            # Determinar el color de la alerta según los meses transcurridos
            if meses_transcurridos >= 12:
                alerta_clase = 'alert alert-danger'  # Rojo: Más de 12 meses (un año o más)
            elif 11 <= meses_transcurridos < 12:
                alerta_clase = 'alert alert-warning'  # Amarillo: Entre 11 y 12 meses (falta un mes o menos)
            else:
                alerta_clase = 'alert alert-success'  # Verde: Menos de 11 meses

            alertas.append({
                'revision': revision,
                'alerta_clase': alerta_clase,
                'meses_transcurridos': meses_transcurridos,
                'dias_restantes': dias_restantes,
                'vencido': vencido,  # Indica si está vencido
            })

        # Añadir la lista de alertas al contexto
        context['alertas'] = alertas
        return context
