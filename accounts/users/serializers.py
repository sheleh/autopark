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
        fields = ['url', 'email', 'first_name', 'last_name', 'is_company_admin',
                  'password', 'company']

