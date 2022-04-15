from django.core.management.base import BaseCommand
from faker import Faker
import random

from ...models import Incoming, AssignedTo

class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(15):
            Incoming.objects.get_or_create(
                title=fake.unique.sentence(nb_words=10),
                author = fake.company(),
                description=fake.text(),
                assigned_to = AssignedTo.objects.get(id=random.randint(1,10))
            )
