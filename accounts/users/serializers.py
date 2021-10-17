from . models import Account
from rest_framework import serializers
from accounts.companies.serializers import CompanySerializer
from accounts.companies.models import Company


class AdminUserCompanyRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_staff = serializers.BooleanField(default=True)
    password = serializers.CharField(required=True)
    password_repeat = serializers.CharField(required=True)

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError('Those passwords dont match')
        return data


class UserSerializer(serializers.ModelSerializer):
    """Company Administrator Serializer"""
    #password_repeat = serializers.SerializerMethodField('get_password_confirmation')
    company = CompanySerializer()

    #def get_password_confirmation(self, password_repeat):
    #    print(password_repeat)
    #    print(self.context)

    def create(self, validated_data):
        #print(validated_data)
        company_data = validated_data.pop('company')
        #print(company_data)
        company = Company.objects.create(**company_data)
        user = Account.objects.create(**validated_data, company_id=company.pk)
        user.set_password(validated_data['password'])
        user.save()
        return user

    #def password_validation(self, validated_data):
    #    password = validated_data['password']
    #    password_confirmation = validated_data['repeat password']
    #    if password != password_confirmation:
    #        raise serializers.ValidationError('Passwords is not a same , please try again')

    #def get_password_confirmation(self, obj):
    #    print(self.context)
    #    print(obj)

    class Meta:
        model = Account
        #repeat_password = serializers.CharField(write_only=True, allow_blank=False)
        fields = ['url', 'email', 'first_name', 'last_name', 'is_staff',
                  'password', 'company']


class EmployeeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        owner_data = self.context.get('owner_data')
        employee = Account.objects.create(**validated_data, owner=owner_data.id, company_id=owner_data.company.pk)
        employee.set_password(validated_data['password'])
        employee.is_staff = False
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        office = validated_data.get('office', instance.office)
        # token always changes when data updates
        instance.set_password(instance.password)
        if office.company == instance.company:
            instance.office = office
            instance.save()
            return instance
        else:
            raise serializers.ValidationError('Wrong office id, please choose another')

    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'office']


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




