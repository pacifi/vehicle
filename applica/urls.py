from django.urls import path
from rest_framework import routers

from applica.apis import ExcesoVelocidadPorMesAPIView
from applica.views import reporte_velocidad

router = routers.SimpleRouter()



app_name = "applica"

urlpatterns = [

    path('reporte/velocidad', reporte_velocidad, name='reporte_velocidad'),
    path('api/excesos-velocidad/<int:year>/', ExcesoVelocidadPorMesAPIView.as_view(), name='excesos-velocidad-por-mes'),

]

urlpatterns = urlpatterns + router.urls
