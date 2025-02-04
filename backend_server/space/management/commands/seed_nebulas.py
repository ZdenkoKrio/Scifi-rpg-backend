from django.core.management.base import BaseCommand
from space.models import Nebula
import random

NEBULA_TYPES = ["hydrogen", "ionized", "radioactive", "unknown"]


class Command(BaseCommand):
    """Seeds the database with nebulas in random locations."""
    help = "Seed the database with nebulas."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding nebulas...")

        nebula_count = 0

        for _ in range(random.randint(5, 15)):
            Nebula.objects.create(
                name=f"Nebula-{nebula_count+1}",
                coordinates_x=random.randint(-10000, 10000),
                coordinates_y=random.randint(-10000, 10000),
                coordinates_z=random.randint(-10000, 10000),
                gas_composition=random.choice(NEBULA_TYPES),
                visibility=random.randint(10, 100),
                has_storms=random.choice([True, False]),
            )
            nebula_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {nebula_count} nebulas!"))