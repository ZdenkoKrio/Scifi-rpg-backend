from django.core.management.base import BaseCommand
from space.models import StarSystem, Planet
import random

ATMOSPHERE_TYPES = ["breathable", "toxic", "none"]
ECONOMY_TYPES = ["trade_hub", "industrial", "agriculture", "military"]


class Command(BaseCommand):
    """Seeds the database with planets for star systems."""
    help = "Seed the database with planets."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding planets...")

        star_systems = StarSystem.objects.all()
        planet_count = 0

        for system in star_systems:
            for _ in range(random.randint(4, 9)):  # 4 to 9 planets per system
                Planet.objects.create(
                    name=f"{system.name} Planet {planet_count+1}",
                    star_system=system,
                    atmosphere_type=random.choice(ATMOSPHERE_TYPES),
                    population=random.randint(0, 1000000000),
                    economy_type=random.choice(ECONOMY_TYPES) if random.random() > 0.2 else None,
                    size=random.randint(3000, 50000),
                )
                planet_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {planet_count} planets!"))
