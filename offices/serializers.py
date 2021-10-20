from rest_framework import serializers
from .models import Office


class OfficeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        current_user_company = self.context['company']
        office = Office.objects.create(**validated_data, company=current_user_company)
        return office

    class Meta:
        model = Office
        fields = ['id', 'name', 'address', 'country', 'city', 'region']

