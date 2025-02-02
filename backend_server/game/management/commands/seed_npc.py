from django.core.management.base import BaseCommand
from game.models.npc import NPC


class Command(BaseCommand):
    """Seeds the database with test NPC characters."""
    help = "Seed the database with test NPCs."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with NPCs...")

        npc_data = [
            {"name": "Trader Xell", "role": "merchant", "faction": "Galactic Trade Union", "dialogue": "I have the best deals in the galaxy!", "reputation_effect": 5},
            {"name": "Captain Raze", "role": "pirate", "faction": "Void Pirates", "dialogue": "Hand over your cargo, or else!", "reputation_effect": -10},
            {"name": "Officer Lyn", "role": "officer", "faction": "Galactic Federation", "dialogue": "We are watching you, citizen.", "reputation_effect": 3},
            {"name": "Doctor Yara", "role": "scientist", "faction": None, "dialogue": "Science is the key to our survival.", "reputation_effect": 0},
            {"name": "Bounty Hunter Kreel", "role": "bounty_hunter", "faction": "Independent", "dialogue": "You have a price on your head.", "reputation_effect": -5},
        ]

        for npc in npc_data:
            NPC.objects.create(**npc)

        self.stdout.write(self.style.SUCCESS("Successfully seeded NPCs!"))
