from django_filters import rest_framework as filters
from . models import Account


class EmployeeFilter(filters.FilterSet):

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email']
