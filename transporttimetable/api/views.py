from django.shortcuts import render
from rest_framework import viewsets
from .models import TransportStop
from .serializers import TransportStopSerializer

class TransportStopViewSet(viewsets.ModelViewSet):
    queryset = TransportStop.objects.all()
    serializer_class = TransportStopSerializer


