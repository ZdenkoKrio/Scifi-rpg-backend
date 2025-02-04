from django.core.management.base import BaseCommand
from diplomation.models import Faction


class Command(BaseCommand):
    """Seeds the database with factions."""
    help = "Populate the database with test factions."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with factions...")

        factions = [
            {"name": "Galactic Federation", "description": "A union of civilized planets promoting peace and order."},
            {"name": "Void Pirates", "description": "A ruthless group of space outlaws raiding star systems."},
            {"name": "AI Overlords", "description": "A synthetic empire ruled by self-aware AI seeking efficiency."},
            {"name": "Independent Colonies", "description": "A collection of autonomous human and alien settlements."},
            {"name": "Shadow Syndicate", "description": "A secretive organization operating in the black markets."},
        ]

        for faction_data in factions:
            Faction.objects.create(**faction_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded factions!"))
