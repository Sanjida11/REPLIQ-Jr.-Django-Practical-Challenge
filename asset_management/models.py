from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_out_devices')
    checked_out_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    returned_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
