from django.urls import path
from rest_framework import routers

from applica.apis import ConductorModelViewSet
from applica.views import reporte_velocidad

router = routers.SimpleRouter()

router.register("conductors", ConductorModelViewSet)

app_name = "applica"

urlpatterns = [

    path('reporte/velocidad', reporte_velocidad, name='reporte_velocidad'),
]

urlpatterns = urlpatterns + router.urls
