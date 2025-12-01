from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransportStopViewSet


router = DefaultRouter()
router.register(r'stops', TransportStopViewSet)
urlpatterns = [
    path('', include(router.urls)),
]