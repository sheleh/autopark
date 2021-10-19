from rest_framework import serializers
from . models import Vehicle
from accounts.users.models import Account
from offices.models import Office


class VehicleSerializer(serializers.ModelSerializer):
    driver = serializers.SlugRelatedField(queryset=Account.objects.all(), slug_field='first_name', required=False)
    office = serializers.SlugRelatedField(queryset=Office.objects.all(), slug_field='name', required=False)

    def create(self, validated_data):
        company_id = self.context.get('company_id')
        vehicle = Vehicle.objects.create(**validated_data, company_id=company_id)
        return vehicle

    def validate_driver_has_office(self):
        driver = self.validated_data.get('driver')
        print(driver)
        if not driver.office:
            raise serializers.ValidationError('Driver not assign to any office')

    def validate_driver_equal_office(self):
        driver = self.validated_data.get('driver')
        office = self.validated_data.get('office')
        if driver.office.id != office.id:
            raise serializers.ValidationError('Driver and Car not in a same office')

    class Meta:
        model = Vehicle
        fields = ['id', 'license_plate', 'name', 'model', 'year_of_manufacture', 'driver', 'office']
