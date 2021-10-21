from django.db import models


class Company(models.Model):
    """Company model"""
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150, blank=True)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
