from django.core.management.base import BaseCommand
from space import StarSystem, SpaceStation, CelestialBody
from diplomation import Faction
import random

STATION_TYPES = ["trading", "military", "research"]


class Command(BaseCommand):
    """Seeds the database with space stations orbiting celestial bodies or free-floating."""
    help = "Seed the database with space stations."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding space stations...")

        star_systems = StarSystem.objects.all()
        factions = list(Faction.objects.all())
        station_count = 0

        for system in star_systems:
            for _ in range(random.randint(0, 3)):  # 0 to 3 stations per system
                orbiting_body = CelestialBody.objects.filter(star_system=system).order_by("?").first()
                owner_faction = random.choice(factions) if factions and random.random() < 0.7 else None

                SpaceStation.objects.create(
                    name=f"{system.name} Station {station_count+1}",
                    star_system=system,
                    station_type=random.choice(STATION_TYPES),
                    owner_faction=owner_faction,
                    orbiting_object=orbiting_body if orbiting_body and random.random() < 0.7 else None,
                )
                station_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {station_count} space stations!"))
