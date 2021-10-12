from . models import Account
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import UserSerializer, EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from . services import EmployeeFilter


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter

    def get_queryset(self):
        current_user = self.request.user
        return Account.objects.filter(owner=current_user.id)

    def get_serializer_context(self):
        """sending authenticated user data to serializer"""
        context = super(EmployeeViewSet, self).get_serializer_context()
        context["owner_data"] = self.request.user
        return context


class ProfileEdit(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        current_user = self.request.user
        return Account.objects.filter(pk=current_user.id)
    pass




