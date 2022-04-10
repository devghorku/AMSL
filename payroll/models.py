from django.db import models


# Create your models here.
from employee.models import Employee


class Payroll(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_date = models.DateTimeField()
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.employee.name
