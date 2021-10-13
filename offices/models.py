from django.db import models
from accounts.companies.models import Company


class Office(models.Model):
    """Office model"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

