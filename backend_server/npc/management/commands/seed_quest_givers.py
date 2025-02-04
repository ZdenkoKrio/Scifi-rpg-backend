from django.core.management.base import BaseCommand
from npc.models import NPC, QuestGiver
from diplomation.models import Faction


class Command(BaseCommand):
    """Seeds the database with Quest Givers."""
    help = "Populate the database with test Quest Givers."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with Quest Givers...")

        quest_givers = [
            {"name": "Oracle Xyra", "faction": "Independent"},
            {"name": "Commander Vex", "faction": "Galactic Federation"},
            {"name": "Captain Sylas", "faction": "Void Pirates"},
            {"name": "Elder Zorak", "faction": "Independent"},
            {"name": "Technomage Selia", "faction": "Independent"},
            {"name": "Agent Mira", "faction": "Galactic Federation"},
            {"name": "Smuggler Jett", "faction": "Void Pirates"},
            {"name": "Colonel Drake", "faction": "Galactic Federation"},
            {"name": "Cyber Mystic", "faction": "Independent"},
            {"name": "Master Haldor", "faction": "Unknown"},
        ]

        for giver in quest_givers:
            faction, _ = Faction.objects.get_or_create(name=giver["faction"], defaults={"description": "Faction description"})
            npc = NPC.objects.create(
                name=giver["name"],
                role="ally",
                level=8,
                faction=faction,
                dialogue=f"I have a mission for you, traveler.",
                reputation_effect=10
            )
            QuestGiver.objects.create(npc=npc)

        self.stdout.write(self.style.SUCCESS("Successfully seeded Quest Givers!"))
