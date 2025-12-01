from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .services.gtfs import get_real_time_feed
from .utils.gtfs import extract_departures

import time
from datetime import UTC, datetime
import pytz

from .models import TransportStop
from .serializers import TransportStopSerializer

class TransportStopViewSet(viewsets.ModelViewSet):
    queryset = TransportStop.objects.all()
    serializer_class = TransportStopSerializer

class DepartingTripsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        stops_qs = TransportStop.objects.all()
        stop_map = {
            str(code): name
            for code, name in stops_qs.values_list("code", "name")
        }
        stop_ids = list(stop_map.keys())

        if not stop_ids:
                return Response(
                    {"error": "No transport stops specified."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        
        try: 
            feed = get_real_time_feed()
        except Exception as e:
            return Response({"error": "Could not retrieve realtime transport feed: {e}."}, status=status.HTTP_502_BAD_GATEWAY)

        next_trips = extract_departures(feed, stop_ids)
        
        result = {}

        for stop_id, trips in next_trips.items():
            trips.sort()
            trips = trips[:3] # TODO: this should be customisable in the future
            
            result[stop_id] = {
                "stop_name": stop_map.get(stop_id),
                "trips": [
                    {
                        "route": route,
                        "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for dt, route in trips
                ],
            }

        return Response(result, status=status.HTTP_200_OK)
