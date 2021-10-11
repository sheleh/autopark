from . models import Account
from rest_framework import serializers
from accounts.companies.serializers import CompanySerializer
from accounts.companies.models import Company


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company = Company.objects.create(**company_data)
        user = Account.objects.create(**validated_data, company_id=company.pk)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Account
        fields = ['url', 'email', 'first_name', 'last_name', 'is_staff',
                  'password', 'company']


class EmployeeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        owner_data = self.context.get('owner_data')
        employee = Account.objects.create(**validated_data, owner=owner_data.id, company_id=owner_data.company.pk)
        employee.set_password(validated_data['password'])
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.set_password(instance.password)
        instance.save()
        return instance

    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


