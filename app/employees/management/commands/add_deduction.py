from django.core.management.base import BaseCommand
from faker import Faker
import random
from decimal import Decimal
from ...models import Employee, Deduction


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Deduction.objects.get_or_create(
                employee = Employee.objects.get(id=random.randint(1,10)),
                d_name = fake.license_plate(),
                d_amount=Decimal(fake.pricetag().replace('$', '').replace(',', '')),
            )