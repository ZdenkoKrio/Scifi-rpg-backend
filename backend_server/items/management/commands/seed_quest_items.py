from django.core.management.base import BaseCommand
from items.models import QuestItem


class Command(BaseCommand):
    """Seeds the database with a set of predefined quest items."""
    help = "Seed the database with quest items."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding quest items...")

        quest_items = [
            {"name": "Ancient Star Map", "rarity": "rare", "quest_name": "The Forgotten System", "is_consumed": False},
            {"name": "Encrypted Data Core", "rarity": "epic", "quest_name": "Spy Network", "is_consumed": True},
            {"name": "Diplomatic Treaty", "rarity": "uncommon", "quest_name": "Galactic Peace Negotiations", "is_consumed": False},
            {"name": "Prototype AI Chip", "rarity": "legendary", "quest_name": "Rise of the Machines", "is_consumed": True},
            {"name": "Time Distortion Beacon", "rarity": "epic", "quest_name": "Chrono Rift Stabilization", "is_consumed": False},
            {"name": "Alien Relic", "rarity": "rare", "quest_name": "Ancient Mysteries", "is_consumed": True},
            {"name": "Void Energy Capsule", "rarity": "uncommon", "quest_name": "Fuel Crisis", "is_consumed": False},
            {"name": "Lost Captain’s Log", "rarity": "common", "quest_name": "Ghost Ship Investigation", "is_consumed": False},
            {"name": "Biohazard Sample", "rarity": "rare", "quest_name": "Plague Containment", "is_consumed": True},
            {"name": "Starship Override Codes", "rarity": "epic", "quest_name": "Infiltration Mission", "is_consumed": False},
        ]

        for quest_item_data in quest_items:
            QuestItem.objects.get_or_create(**quest_item_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded quest items!"))
