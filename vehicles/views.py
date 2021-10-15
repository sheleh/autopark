from .serializers import VehicleSerializer
from .models import Vehicle
from rest_framework import viewsets, status, permissions, mixins


class ListCreateVehicle(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.IsAdminUser]
