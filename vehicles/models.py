from django.db import models
from accounts.users.models import Account
from offices.models import Office


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_of_manufacture = models.DateField()
    driver = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.license_plate


