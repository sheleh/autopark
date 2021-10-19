from rest_framework import serializers
from .models import Office
from django.shortcuts import get_object_or_404


class OfficeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        current_user_company = self.context
        office = Office.objects.create(**validated_data, company=current_user_company)
        return office

    class Meta:
        model = Office
        fields = ['name', 'address', 'country', 'city', 'region']

