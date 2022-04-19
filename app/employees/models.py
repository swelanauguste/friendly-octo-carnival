from django.db import models


class Employee(models.Model):
    employee_uid = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.employee_uid} - {self.first_name} {self.last_name}"


class Deduction(models.Model):
    employee = models.ForeignKey(
        Employee, related_name="deductions", on_delete=models.CASCADE
    )
    d_name = models.CharField(max_length=100)
    d_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee.first_name} - ${self.d_amount}"
