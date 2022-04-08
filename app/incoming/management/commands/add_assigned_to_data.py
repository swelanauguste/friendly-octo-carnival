from django.core.management.base import BaseCommand
from faker import Faker
import random

from ...models import AssignedTo
from users.models import User


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(4):
            AssignedTo.objects.get_or_create(
                name=fake.unique.company(), 
                # description=fake.text()
            )
