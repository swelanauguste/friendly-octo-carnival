from decimal import Decimal
from statistics import mode

from django.db import models
from employees.models import Employee
from users.models import User


class DeductionChange(models.Model):
    """
    DeductionChange model
    """

    employee = models.ForeignKey(
        Employee, related_name="employees", on_delete=models.CASCADE
    )
    pay_element_code = models.CharField(max_length=255)
    change_amount = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    payment_period = models.PositiveIntegerField(
        default=1, help_text="<em>No. of months</em>"
    )
    change_reason = models.CharField(max_length=255)
    remarks = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User, related_name="deduction_change_created_by", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, related_name="deduction_change_updated_by", on_delete=models.CASCADE
    )

    @property
    def get_monthly_payment(self):
        chng_amt = self.change_amount.replace(",", "").replace("$", "")
        chng_amt_rnd = round(Decimal(chng_amt) / self.payment_period, 2)
        return f'${chng_amt_rnd}'

    def __str__(self):
        return f"{self.employee.employee_uid}, {self.change_amount}, {self.start_date}, {self.end_date}"
