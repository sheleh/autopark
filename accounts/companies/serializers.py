from rest_framework import serializers
from . models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address']

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data['name']
        print(validated_data['name'])
        instance.address = validated_data['address']
        return super().update(instance, validated_data)



