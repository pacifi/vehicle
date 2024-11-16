from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from applica.models import Conductor, ExcesoVelocidad, Incidencia, Infraccion
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


class ExcesoVelocidadPorVehiculoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener parámetros de la solicitud
        print(self.kwargs)
        # Filtrar infracciones por año y mes
        registros = (
            ExcesoVelocidad.objects
            .filter(fecha_evento__year=self.kwargs['year'], fecha_evento__month=self.kwargs['month'])
            .values('vehiculo__id', 'vehiculo__placa')  # Suponiendo que Vehiculo tiene un campo 'placa'
            .annotate(cantidad=Count('id'))
            .order_by('-cantidad')
        )

        # Crear listas de vehículos y sus infracciones
        vehiculos = []
        infracciones = []

        for registro in registros:
            vehiculos.append(registro['vehiculo__placa'])
            infracciones.append(registro['cantidad'])

        # Respuesta con dos listas
        return Response({"vehiculos": vehiculos, "infracciones": infracciones})


class IncidenciaPorMesAPIView(APIView):
    def get(self, request, year=2024):
        # Filtrar por año usando `fecha_evento__year`
        registros = (
            Incidencia.objects
            .filter(fecha_incidencia__year=year)
            .annotate(mes=TruncMonth('fecha_incidencia'))
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


class IncidenciaPorConductorAPIView(APIView):
    def get(self, request, year, month):
        # Filtrar incidencias por el año y mes proporcionados
        registros = (
            Incidencia.objects
            .filter(fecha_incidencia__year=year, fecha_incidencia__month=month)
            .values('conductor__id', 'conductor__nombre')  # Agrupar por conductor
            .annotate(cantidad=Count('id'))  # Contar incidencias por conductor
            .order_by('-cantidad')  # Ordenar por cantidad de incidencias
        )

        # Crear listas de conductores y sus incidencias
        conductores = []
        incidencias = []

        for registro in registros:
            conductores.append(registro['conductor__nombre'])  # Nombre del conductor
            incidencias.append(registro['cantidad'])  # Total de incidencias

        # Respuesta con las dos listas
        return Response({"conductores": conductores, "incidencias": incidencias})


class InfraccionPorMesAPIView(APIView):
    def get(self, request, year=2024):
        # Filtrar por año usando `fecha_evento__year`
        registros = (
            Infraccion.objects
            .filter(fecha_infraccion__year=year)
            .annotate(mes=TruncMonth('fecha_infraccion'))
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


class InfraccionPorConductorAPIView(APIView):
    def get(self, request, year, month):
        # Filtrar incidencias por el año y mes proporcionados
        registros = (
            Infraccion.objects
            .filter(fecha_infraccion__year=year, fecha_infraccion__month=month)
            .values('conductor__id', 'conductor__nombre')  # Agrupar por conductor
            .annotate(cantidad=Count('id'))  # Contar incidencias por conductor
            .order_by('-cantidad')  # Ordenar por cantidad de incidencias
        )

        # Crear listas de conductores y sus incidencias
        conductores = []
        incidencias = []

        for registro in registros:
            conductores.append(registro['conductor__nombre'])  # Nombre del conductor
            incidencias.append(registro['cantidad'])  # Total de incidencias

        # Respuesta con las dos listas
        return Response({"conductores": conductores, "incidencias": incidencias})
