from django.core.management.base import BaseCommand
from diplomation.models import Species
from space.models import Planet


class Command(BaseCommand):
    """Seeds the database with species."""
    help = "Populate the database with test species."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with species...")

        earth = Planet.objects.filter(name="Earth").first()
        mars = Planet.objects.filter(name="Mars").first()
        unknown = None

        species_list = [
            {"name": "Humans", "species_type": "intelligent", "homeworld": earth, "lifespan": 80, "average_height": 1.75, "description": "Adaptive and resourceful."},
            {"name": "Martians", "species_type": "intelligent", "homeworld": mars, "lifespan": 120, "average_height": 2.1, "description": "Tall, thin beings adapted to low gravity."},
            {"name": "Xel'Naga", "species_type": "intelligent", "homeworld": unknown, "lifespan": 500, "average_height": 2.5, "description": "Ancient celestial beings with vast knowledge."},
            {"name": "Cyber Drones", "species_type": "synthetic", "homeworld": unknown, "lifespan": 1000, "average_height": 1.8, "description": "Self-replicating AI drones built for efficiency."},
            {"name": "Reptilians", "species_type": "primitive", "homeworld": unknown, "lifespan": 200, "average_height": 2.0, "description": "Cold-blooded hunters from an unknown jungle planet."},
        ]

        for species_data in species_list:
            Species.objects.create(**species_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded species!"))
