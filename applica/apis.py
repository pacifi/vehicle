from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from applica.models import Conductor, ExcesoVelocidad
from applica.serializers import ConductorSerializer


class ExcesoVelocidadPorMesAPIView(APIView):
    def get(self, request, year=2024):
        # Filtrar por año usando `fecha_evento__year`
        registros = (
            ExcesoVelocidad.objects
            .filter(fecha_evento__year=year)
            .annotate(mes=TruncMonth('fecha_evento'))
            .values('mes')
            .annotate(cantidad=Count('id'))
            .order_by('mes')
        )

        # Crear un diccionario para contar registros por cada mes del año
        conteo_mensual = {mes: 0 for mes in range(1, 13)}

        for registro in registros:
            mes = registro['mes'].month
            conteo_mensual[mes] = registro['cantidad']

        # Convertir el conteo a una lista en el formato deseado
        respuesta = [conteo_mensual[mes] for mes in range(1, 13)]

        return Response(respuesta)
