from rest_framework import viewsets, status, permissions, mixins
from .serializers import OfficeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Office
from .services import OfficeFilter
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class OfficesView(viewsets.ModelViewSet):
    """Provide Create office / Get list of company offices"""
    serializer_class = OfficeSerializer
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Office.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OfficeFilter

    def get_permissions(self):
        """Set custom permission for each action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'retrieve']:
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action in ['list']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        """Provide view current company offices only"""
        queryset = self.filter_queryset(self.get_queryset().filter(company=self.request.user.company.id))
        serializer = OfficeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        current_user_company = self.request.user.company
        serializer = OfficeSerializer(context={'company': current_user_company}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# adminofficeViewSEt

#has object permission

# Делаю MODELVIEWSET


#class EditOffice(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#    serializer_class = OfficeSerializer
#    permission_classes = [permissions.IsAdminUser]
#
#    def get_queryset(self):
#        """Provide access to current company offices only"""
#        current_company = self.request.user.company
#        queryset = Office.objects.filter(company=current_company.id)
#        return queryset


class ViewOffice(viewsets.ReadOnlyModelViewSet):
    """View office Details"""
    permissions = [permissions.IsAuthenticated, ]
    serializer_class = OfficeSerializer

    def get_queryset(self):
        current_user = self.request.user
        if not current_user.office:
            raise ValidationError({'Message': 'current user not assigned to any office'})
        else:
            office_obj = Office.objects.filter(pk=current_user.office.id)
            return office_obj

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
