from . models import Account
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import UserSerializer, EmployeeSerializer, ProfileViewEditSerializer, AdminUserCompanyRegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from . services import EmployeeFilter
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """Create Company Administrator and Company"""
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['POST']

    def create(self, request, *args, **kwargs):
        serializer = AdminUserCompanyRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeViewSet(viewsets.ModelViewSet):
    """Create, View , Edit worker information"""
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


class ProfileEdit(generics.RetrieveUpdateAPIView):
    """View and edit self information"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileViewEditSerializer
    queryset = Account.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        current_user = self.request.user
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=current_user.id)
        return obj






