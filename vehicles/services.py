import django_filters
from .models import Vehicle


class VehicleFilter(django_filters.rest_framework.FilterSet):
    """ Filter by driver first name , office name """
    office = django_filters.CharFilter(field_name='office__name')
    driver = django_filters.CharFilter(field_name='driver__first_name')

    class Meta:
        model = Vehicle
        fields = ['driver', 'office']

