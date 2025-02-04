from django.core.management.base import BaseCommand
from space.models import StarSystem, UnknownObject
import random

UNKNOWN_TYPES = ["black_hole", "anomaly", "derelict_station", "alien_artifact", "wormhole"]


class Command(BaseCommand):
    """Seeds the database with unknown objects in space."""
    help = "Seed the database with unknown objects."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding unknown objects...")

        star_systems = StarSystem.objects.all()
        unknown_count = 0

        for system in star_systems:
            if random.random() < 0.3:  # 30% chance for unknown object in system
                UnknownObject.objects.create(
                    name=f"{system.name} Unknown Object {unknown_count+1}",
                    star_system=system,
                    coordinates_x=random.uniform(-10000, 10000),
                    coordinates_y=random.uniform(-10000, 10000),
                    coordinates_z=random.uniform(-10000, 10000),
                    object_type=random.choice(UNKNOWN_TYPES),
                    danger_level=random.randint(0, 100),
                    scientific_value=random.randint(10, 100),
                    can_interact=random.choice([True, False]),
                    size=random.randint(300, 50000)
                )
                unknown_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {unknown_count} unknown objects!"))
