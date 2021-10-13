from django_filters import rest_framework as filters
from . models import Office


class OfficeFilter(filters.FilterSet):
    """" Filter by country , city """
    class Meta:
        model = Office
        fields = ['country', 'city']

