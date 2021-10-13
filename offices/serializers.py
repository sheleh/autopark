from rest_framework import serializers
from .models import Office


class OfficeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user_data = self.context
        office = Office.objects.create(**validated_data, company=user_data.company)
        return office

    class Meta:
        model = Office
        fields = ['name', 'address', 'country', 'city', 'region']

