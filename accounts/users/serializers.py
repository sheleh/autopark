from . models import Account
from rest_framework import serializers
from accounts.companies.serializers import CompanySerializer
from accounts.companies.models import Company
from django.contrib.auth.password_validation import validate_password


class PasswordCheckSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    password_repeat = serializers.CharField(required=True)

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError('Those passwords dont match')
        validate_password(password=data.get('password'))
        return data


class UserSerializer(serializers.ModelSerializer):
    """Company Administrator Serializer"""
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
        extra_kwargs = {
            'company': {'write_only': True}
        }


class EmployeeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        owner_data = self.context.get('owner_data')
        office = self.validated_data.get('office')
        if office and owner_data.company.id != office.company.id:
            raise serializers.ValidationError('Wrong office id, please choose another')
        else:
            employee = Account.objects.create(**validated_data, owner=owner_data.id,
                                              company_id=owner_data.company.pk)
            employee.set_password(validated_data['password'])
            employee.is_staff = False
            employee.save()
            return employee

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('password'):
            password = validated_data.get('password')
            instance.set_password(password)
        office = validated_data.get('office', instance.office)
        if office:
            if office.company != instance.company:
                raise serializers.ValidationError('Wrong office id, please choose another')
            instance.office = office
        instance.save()
        return instance

    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'office']
        extra_kwargs = {'password': {'write_only': True}}


class ProfileViewEditSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('password') is not None:
            instance.password = validated_data.pop('password')
            instance.set_password(instance.password)
            instance.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}




