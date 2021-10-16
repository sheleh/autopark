import django_filters
from django_filters import rest_framework as filters
from .models import Vehicle
from accounts.users.models import Account
from offices.models import Office


class VehicleFilter(django_filters.rest_framework.FilterSet):
    #driver = django_filters.ModelChoiceFilter(queryset=Account.objects.all())
    #print(driver.__str__())
    #office = django_filters.CharFilter(field_name='office__name', lookup_expr='iexact')


    class Meta:
        model = Vehicle
        fields = ['name']

