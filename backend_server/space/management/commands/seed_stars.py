from django.core.management.base import BaseCommand
from space import StarSystem, Star
import random

STAR_TYPES = ["main_sequence", "red_giant", "white_dwarf", "neutron", "black_hole"]


class Command(BaseCommand):
    """Seeds the database with stars for each star system."""
    help = "Seed the database with stars."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding stars...")

        star_systems = StarSystem.objects.all()
        for system in star_systems:
            Star.objects.create(
                name=f"{system.name} Star",
                star_system=system,
                star_type=random.choice(STAR_TYPES),
                temperature=random.randint(3000, 25000),
                size=random.randint(10, 5000),
                luminosity=random.uniform(0.1, 100),
            )

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(star_systems)} stars!"))
