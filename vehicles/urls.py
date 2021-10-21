from rest_framework import routers
from django.urls import path, include
from . views import AdminVehicleViewSet, ViewListVehicle

router = routers.DefaultRouter()
router.register('vehicle_create_edit', AdminVehicleViewSet, basename='vehicle_create_edit')
router.register(r'vehicles_view', ViewListVehicle, basename='vehicles_view')

urlpatterns = [
    path('', include(router.urls)),
]
