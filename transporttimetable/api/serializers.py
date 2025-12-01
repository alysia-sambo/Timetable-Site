from rest_framework import serializers
from .models import TransportStop

class TransportStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportStop
        fields = '__all__'