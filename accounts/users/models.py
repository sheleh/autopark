from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from accounts.companies.models import Company


class Account(AbstractBaseUser):
    """Custom User Model"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_company_admin = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    #owner = models.IntegerField(default=None)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company']

    def __str__(self):
        return self.email

