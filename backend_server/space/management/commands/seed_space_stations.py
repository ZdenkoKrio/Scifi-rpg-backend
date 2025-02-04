from django.core.management.base import BaseCommand
from space.models import StarSystem, SpaceStation, Planet, Moon, Asteroid
from diplomation.models import Faction
from django.contrib.contenttypes.models import ContentType
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
            celestial_bodies = list(Planet.objects.filter(star_system=system))

            celestial_bodies += list(Moon.objects.filter(planet__star_system=system))

            celestial_bodies += list(Asteroid.objects.filter(star_system=system))

            for _ in range(random.randint(0, 3)):
                orbiting_body = random.choice(celestial_bodies) if celestial_bodies and random.random() < 0.7 else None
                owner_faction = random.choice(factions) if factions and random.random() < 0.7 else None

                station = SpaceStation.objects.create(
                    name=f"{system.name} Station {station_count+1}",
                    star_system=system,
                    station_type=random.choice(STATION_TYPES),
                    owner_faction=owner_faction,
                )

                if orbiting_body:
                    station.orbiting_content_type = ContentType.objects.get_for_model(orbiting_body)
                    station.orbiting_object_id = orbiting_body.id
                    station.save()

                station_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {station_count} space stations!"))
