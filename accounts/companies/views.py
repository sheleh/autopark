from . models import Company
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

