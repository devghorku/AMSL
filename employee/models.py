from django.db import models


# Create your models here.
class EmployeeCategory(models.Model):
    name = models.CharField(unique=True, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Employee(models.Model):
    category = models.ForeignKey(EmployeeCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    employee_id = models.CharField(null=True, max_length=50)
    nid = models.CharField(null=True, max_length=50)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-active']

    def __str__(self):
        return self.name