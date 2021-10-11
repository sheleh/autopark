from . models import Company
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import CompanySerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404


class CompanyEditViewSet(generics.UpdateAPIView):
    """
    API endpoint that allows Company to be edited.
    """
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Company.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        current_user = self.request.user
        objects = self.get_queryset()
        return get_object_or_404(objects, pk=current_user.company.id)


class CompanyView(viewsets.ReadOnlyModelViewSet):
    """
    View only Company details
    """
    # queryset = Company.objects.get(pk=1) WHY?  AttributeError: 'Company' object has no attribute 'model'
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Company.objects.filter(pk=current_user.company.id)
