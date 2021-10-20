from . models import Company
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import CompanySerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404


class CompanyEditView(generics.UpdateAPIView):
    """
    API endpoint that allows Company to be edited.
    """
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Company.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        """Returns an object instance that should be used for detail views"""
        current_user = self.request.user
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=current_user.company.id)
        return obj


class CompanyView(viewsets.ReadOnlyModelViewSet):
    """
    View only Current user's company details
    """
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        return Company.objects.filter(pk=current_user.company.id)
