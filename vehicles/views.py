from .serializers import VehicleSerializer
from .models import Vehicle
from rest_framework import viewsets, status, permissions, mixins
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from . services import VehicleFilter


#class ListCreateVehicle(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
#    """Create vehicle and view List of company vehicles"""
#    serializer_class = VehicleSerializer
#    queryset = Vehicle.objects.all()
#    permission_classes = [permissions.IsAdminUser]
#    filter_backends = [DjangoFilterBackend]
#    filterset_class = VehicleFilter

#    def get_queryset(self):
#        current_user_company = self.request.user.company.id
#        return Vehicle.objects.filter(company=current_user_company)

    #def list(self, request, *args, **kwargs):
    #    current_user_company = self.request.user.company.id
    #    #queryset = get_list_or_404(Vehicle, company=current_user_company)
    #    queryset = Vehicle.objects.filter(company=current_user_company)
    #    serializer = VehicleSerializer(queryset, many=True)
    #    return Response(serializer.data)

#    def create(self, request, *args, **kwargs):
#        company_id = self.request.user.company.id
#        serializer = VehicleSerializer(data=request.data, context={'company_id': company_id})
#        if serializer.is_valid():
#            serializer.validate_driver_equal_office()
#            serializer.save()
#            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter

    def get_queryset(self):
        current_user_company = self.request.user.company.id
        return Vehicle.objects.filter(company=current_user_company)

    def create(self, request, *args, **kwargs):
        company_id = self.request.user.company.id
        serializer = VehicleSerializer(data=request.data, context={'company_id': company_id})
        if serializer.is_valid(raise_exception=True):
            if request.data.get('driver') and request.data.get('office'):
                serializer.validate_driver_has_office()
                serializer.validate_driver_equal_office()
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ViewListVehicle(viewsets.ReadOnlyModelViewSet):
    """View List of current User Vehicles"""
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user.id
        user_vehicles = Vehicle.objects.filter(driver=current_user)
        return user_vehicles

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

