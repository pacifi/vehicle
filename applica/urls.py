from debug_toolbar.panels.alerts import AlertsPanel
from django.urls import path
from rest_framework import routers

from applica.apis import ExcesoVelocidadPorMesAPIView, IncidenciaPorMesAPIView, ExcesoVelocidadPorVehiculoAPIView, \
    IncidenciaPorConductorAPIView
from applica.views import ReporteVelcidadTemplateView, AlertaRevisionTecnicaTemplateView, \
    ReporteIncidenciasTemplateView, \
    AlertaSoatTemplateView, ReporteIncidenciasChoferTemplateView, ReporteVelcidadVehiculoTemplateView

router = routers.SimpleRouter()

app_name = "applica"

urlpatterns = [

    path('reporte/alerta-revision', AlertaRevisionTecnicaTemplateView.as_view(), name='reporte_alerta_revision'),
    path('reporte/alerta-soat', AlertaSoatTemplateView.as_view(), name='reporte_alerta_soat'),
    path('reporete/incidencias', ReporteIncidenciasTemplateView.as_view(), name='reporte_incidencias'),
    path('reporete/incidencias-chofer', ReporteIncidenciasChoferTemplateView.as_view(),
         name='reporte_chofer_incidencias'),
    path('reporte/velocidad-vehiculo', ReporteVelcidadVehiculoTemplateView.as_view(),
         name='reporte_vehiculo_velocidad'),
    path('reporte/velocidad', ReporteVelcidadTemplateView.as_view(),
         name='reporte_velocidad'),

    path('api/excesos-velocidad/<int:year>/', ExcesoVelocidadPorMesAPIView.as_view(), name='excesos-velocidad-por-mes'),
    path('api/excesos-velocidad-vehiculo/<int:year>/<str:month>/', ExcesoVelocidadPorVehiculoAPIView.as_view(),
         name='incidencias-por-vehiculo'),
    path('api/insidencias/<int:year>/', IncidenciaPorMesAPIView.as_view(), name='incidencias-por-mes'),
    path('api/insidencias-conductor/<int:year>/<str:month>/', IncidenciaPorConductorAPIView.as_view(),
         name='incidencias-por-conductor'),

]

urlpatterns = urlpatterns + router.urls
