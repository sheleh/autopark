import django_filters
from django_filters import rest_framework as filters
from .models import Vehicle
from accounts.users.models import Account
from offices.models import Office


class VehicleFilter(django_filters.rest_framework.FilterSet):
    """ Filter by driver first name , office name """
    office = django_filters.CharFilter(field_name='office__name')
    driver = django_filters.CharFilter(field_name='driver__first_name')

    class Meta:
        model = Vehicle
        fields = ['driver', 'office']

