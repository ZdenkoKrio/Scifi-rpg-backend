from django.core.management.base import BaseCommand
from space.models import StarSystem, Asteroid
import random


class Command(BaseCommand):
    """Seeds the database with asteroids for star systems."""
    help = "Seed the database with asteroids."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding asteroids...")

        star_systems = StarSystem.objects.all()
        asteroid_count = 0

        for system in star_systems:
            for _ in range(random.randint(2, 6)):  # 2 to 6 asteroids per system
                Asteroid.objects.create(
                    name=f"{system.name} Asteroid {asteroid_count+1}",
                    star_system=system,
                    is_mining_site=random.choice([True, False]),
                    has_pirate_activity=random.choice([True, False]),
                    size=random.randint(3000, 50000)
                )
                asteroid_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {asteroid_count} asteroids!"))