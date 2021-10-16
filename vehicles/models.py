from django.db import models
from accounts.users.models import Account
from offices.models import Office
from accounts.companies.models import Company
from django.core.validators import MinValueValidator


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_of_manufacture = models.IntegerField(validators=[MinValueValidator(1885)])
    driver = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.license_plate


