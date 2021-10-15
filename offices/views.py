from rest_framework import viewsets, status, permissions, mixins
from .serializers import OfficeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Office
from .services import OfficeFilter
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class CreateOfficeView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    """Provide Create office / Get list of company offices"""
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Office.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfficeFilter

    def list(self, request, *args, **kwargs):
        """Provide view current company offices only"""
        queryset = Office.objects.filter(company=self.request.user.company.id)
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            user_data = self.request.user
            serializer = OfficeSerializer(context=user_data, data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditOffice(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        """Provide access to current company offices only"""
        current_company = self.request.user.company
        queryset = Office.objects.filter(company=current_company.id)
        return queryset


class ViewOffice(viewsets.ReadOnlyModelViewSet):
    """View office Details"""
    permissions = [permissions.IsAuthenticated, ]
    serializer_class = OfficeSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.office is None:
            raise ValidationError({'Message': 'current user not assigned to any office'})
        else:
            office_obj = Office.objects.filter(pk=current_user.office.id)
            return office_obj




