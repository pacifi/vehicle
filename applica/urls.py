from debug_toolbar.panels.alerts import AlertsPanel
from django.urls import path
from rest_framework import routers

from applica.apis import ExcesoVelocidadPorMesAPIView
from applica.views import ReporteVelcidadTemplateView, RevisionTecnicaTemplateView, ReporteIncidenciasTemplateView

router = routers.SimpleRouter()

app_name = "applica"

urlpatterns = [

    path('reporte/velocidad', ReporteVelcidadTemplateView.as_view(), name='reporte_velocidad'),
    path('reporte/alerta-revision', RevisionTecnicaTemplateView.as_view(), name='reporte_alerta_revision'),
    path('reporete/incidencias', ReporteIncidenciasTemplateView.as_view(), name='reporte_incidencias'),
    path('api/excesos-velocidad/<int:year>/', ExcesoVelocidadPorMesAPIView.as_view(), name='excesos-velocidad-por-mes'),

]

urlpatterns = urlpatterns + router.urls
