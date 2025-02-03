from django.core.management.base import BaseCommand
from game.models import Species, Faction, SpeciesFaction
from game.models import StarSystem, Planet


class Command(BaseCommand):
    """Seeds the database with factions, species, and their relationships."""
    help = "Seed the database with factions, species, and their relationships."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with diplomacy-related data...")

        # Fetch or create some star systems and planets
        sol_system, _ = StarSystem.objects.get_or_create(name="Sol", coordinates_x=0, coordinates_y=0, coordinates_z=0)
        earth, _ = Planet.objects.get_or_create(name="Earth", defaults={"star_system": sol_system, "size": 100, "atmosphere_type": "breathable", "population": 8000000000})

        # Create factions
        federation = Faction.objects.create(name="Galactic Federation", description="A coalition of peaceful civilizations.", capital_system=sol_system)
        empire = Faction.objects.create(name="Xel'Rath Empire", description="A militaristic and expansionist regime.")

        # Create species
        humans = Species.objects.create(name="Humans", species_type="intelligent", homeworld=earth, lifespan=90, average_height=1.8, description="Dominant species on Earth.")
        xel_rath = Species.objects.create(name="Xel'Rath", species_type="intelligent", lifespan=150, average_height=2.2, description="Reptilian warriors from the Xel'Rath system.")

        # Create faction-species relationships
        SpeciesFaction.objects.create(species=humans, faction=federation, role_in_faction="majority")
        SpeciesFaction.objects.create(species=xel_rath, faction=empire, role_in_faction="rulers")

        self.stdout.write(self.style.SUCCESS("Successfully seeded diplomacy-related data!"))
