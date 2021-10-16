from rest_framework import serializers
from . models import Vehicle
from django.core.validators import MaxValueValidator
from datetime import date
from accounts.users.serializers import EmployeeSerializer
from accounts.users.models import Account
from offices.models import Office


class VehicleSerializer(serializers.ModelSerializer):
    year_of_manufacture = serializers.IntegerField(validators=[MaxValueValidator(int(date.today().year))])
    #driver = serializers.StringRelatedField(read_only=True)
    driver = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field='email')
    office = serializers.SlugRelatedField(queryset=Office.objects.all(), slug_field='name')

    def create(self, validated_data):
        company_id = self.context.get('company_id')
        vehicle = Vehicle.objects.create(**validated_data, company_id=company_id)
        return vehicle

    def validate_driver_equal_office(self):
        driver = self.validated_data.get('driver')
        office = self.validated_data.get('office')
        if driver.office.id != office.id:
            raise serializers.ValidationError('Driver and Car not in a same office')

    class Meta:
        model = Vehicle
        fields = ['license_plate', 'name', 'model', 'year_of_manufacture', 'driver', 'office']
