from django.core.management.base import BaseCommand
from space import StarSystem
from diplomation import Faction
import random


class Command(BaseCommand):
    """Seeds the database with 20 star systems."""
    help = "Seed the database with star systems."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding star systems...")

        factions = list(Faction.objects.all())
        star_systems = []

        for i in range(20):
            faction = random.choice(factions) if factions else None
            star_system = StarSystem.objects.create(
                name=f"System-{i+1}",
                faction=faction,
                coordinates_x=random.uniform(-1000, 1000),
                coordinates_y=random.uniform(-1000, 1000),
                coordinates_z=random.uniform(-1000, 1000),
            )
            star_systems.append(star_system)

        self.stdout.write(self.style.SUCCESS(f"✅ Created {len(star_systems)} star systems!"))
