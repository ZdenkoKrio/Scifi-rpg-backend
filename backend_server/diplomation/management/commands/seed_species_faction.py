from django.core.management.base import BaseCommand
from diplomation import Species, Faction, SpeciesFaction


class Command(BaseCommand):
    """Seeds the database with species-faction relationships."""
    help = "Populate the database with predefined species-faction relations."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with species-faction relationships...")

        humans = Species.objects.filter(name="Humans").first()
        martians = Species.objects.filter(name="Martians").first()
        xelnaga = Species.objects.filter(name="Xel'Naga").first()
        cyber_drones = Species.objects.filter(name="Cyber Drones").first()
        reptilians = Species.objects.filter(name="Reptilians").first()

        federation = Faction.objects.filter(name="Galactic Federation").first()
        pirates = Faction.objects.filter(name="Void Pirates").first()
        ai_overlords = Faction.objects.filter(name="AI Overlords").first()
        independents = Faction.objects.filter(name="Independent Colonies").first()
        syndicate = Faction.objects.filter(name="Shadow Syndicate").first()

        relations = [
            {"species": humans, "faction": federation, "role_in_faction": "majority"},
            {"species": martians, "faction": federation, "role_in_faction": "minority"},
            {"species": xelnaga, "faction": independents, "role_in_faction": "rulers"},
            {"species": cyber_drones, "faction": ai_overlords, "role_in_faction": "majority"},
            {"species": reptilians, "faction": pirates, "role_in_faction": "slaves"},
            {"species": cyber_drones, "faction": federation, "role_in_faction": "minority"},
            {"species": humans, "faction": syndicate, "role_in_faction": "minority"},
            {"species": reptilians, "faction": independents, "role_in_faction": "minority"},
            {"species": martians, "faction": pirates, "role_in_faction": "rulers"},
            {"species": cyber_drones, "faction": syndicate, "role_in_faction": "slaves"},
        ]

        for relation in relations:
            if relation["species"] and relation["faction"]:  
                SpeciesFaction.objects.create(**relation)

        self.stdout.write(self.style.SUCCESS("Successfully seeded species-faction relationships!"))