from django.core.management.base import BaseCommand
from space import Planet, Moon
import random


class Command(BaseCommand):
    """Seeds the database with moons for planets."""
    help = "Seed the database with moons."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding moons...")

        planets = Planet.objects.all()
        moon_count = 0

        for planet in planets:
            for _ in range(random.randint(0, 6)):  # 0 to 6 moons per planet
                Moon.objects.create(
                    name=f"{planet.name} Moon {moon_count+1}",
                    planet=planet,
                    composition=random.choice(["rocky", "metallic", "ice"]),
                    resource_richness=random.randint(0, 100),
                )
                moon_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {moon_count} moons!"))