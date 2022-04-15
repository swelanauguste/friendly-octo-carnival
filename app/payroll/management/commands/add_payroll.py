import random

from django.core.management.base import BaseCommand
from employees.models import Employee
from faker import Faker
from users.models import User

from ...models import DeductionChange


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(15):
            # print(fake.date_this_month())
            # print(fake.future_date())
            DeductionChange.objects.get_or_create(
                employee = Employee.objects.get(id=random.randint(1,10)),
                pay_element_code = fake.cryptocurrency_code(),
                change_amount=fake.pricetag(),
                start_date = fake.future_date(),
                end_date = fake.future_date(),
                payment_period = random.randint(1,12),
                change_reason = fake.sentence(nb_words=10),
                created_by = User.objects.get(pk=1),
                updated_by = User.objects.get(pk=1),
            )
