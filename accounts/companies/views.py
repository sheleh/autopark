from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.AllowAny]

