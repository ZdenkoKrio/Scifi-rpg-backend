from django.core.management.base import BaseCommand
from space import StarSystem, Nebula
import random

NEBULA_TYPES = ["hydrogen", "ionized", "radioactive", "unknown"]


class Command(BaseCommand):
    """Seeds the database with nebulas in star systems."""
    help = "Seed the database with nebulas."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding nebulas...")

        star_systems = StarSystem.objects.all()
        nebula_count = 0

        for system in star_systems:
            if random.random() < 0.4:  # 40% chance for nebula in system
                Nebula.objects.create(
                    name=f"{system.name} Nebula",
                    star_system=system,
                    gas_composition=random.choice(NEBULA_TYPES),
                    visibility=random.randint(10, 100),
                    resource_richness=random.randint(0, 100),
                    has_storms=random.choice([True, False]),
                )
                nebula_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {nebula_count} nebulas!"))
