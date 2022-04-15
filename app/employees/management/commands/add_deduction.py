from django.core.management.base import BaseCommand
from faker import Faker
import random

from ...models import Employee


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        amt = fake.pricetag().replace('$', '').replace(',', '')
        print(amt)
        # for _ in range(10):