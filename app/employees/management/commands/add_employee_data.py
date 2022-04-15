from django.core.management.base import BaseCommand
from faker import Faker
import random

from ...models import Employee


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Employee.objects.get_or_create(
                employee_uid=fake.unique.ssn(), 
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                other_names=fake.last_name(),
            )
