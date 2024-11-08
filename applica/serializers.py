from rest_framework import serializers

from applica.models import Conductor


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'
