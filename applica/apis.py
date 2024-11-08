from rest_framework import viewsets

from applica.models import Conductor
from applica.serializers import ConductorSerializer


class ConductorModelViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
