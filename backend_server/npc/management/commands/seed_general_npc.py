from django.core.management.base import BaseCommand
from npc.models import NPC
from diplomation.models import Faction


class Command(BaseCommand):
    """Seeds the database with general NPCs (bounty hunters, officers, pirates, scientists, etc.)."""
    help = "Populate the database with test general NPCs."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with general NPCs...")

        npcs = [
            {"name": "Captain Drax", "role": "pirate", "level": 5, "faction": "Void Pirates"},
            {"name": "Sergeant Kellan", "role": "officer", "level": 4, "faction": "Galactic Federation"},
            {"name": "Dr. Nova", "role": "scientist", "level": 6, "faction": "Independent"},
            {"name": "Raider Zek", "role": "bounty_hunter", "level": 7, "faction": "Void Pirates"},
            {"name": "Agent Voss", "role": "officer", "level": 3, "faction": "Galactic Federation"},
            {"name": "Lt. Soran", "role": "officer", "level": 5, "faction": "Galactic Federation"},
            {"name": "Nomad Xir", "role": "pirate", "level": 6, "faction": "Void Pirates"},
            {"name": "Professor Elara", "role": "scientist", "level": 8, "faction": "Independent"},
            {"name": "Hunter Gorr", "role": "bounty_hunter", "level": 4, "faction": "Void Pirates"},
            {"name": "Cyber Tinker", "role": "scientist", "level": 7, "faction": "Independent"},
            {"name": "Shadow Warden", "role": "enemy", "level": 9, "faction": "Unknown"},
            {"name": "Commander Ryvek", "role": "officer", "level": 10, "faction": "Galactic Federation"},
            {"name": "Exiled Rogue", "role": "enemy", "level": 6, "faction": "Unknown"},
            {"name": "Technomancer Zen", "role": "scientist", "level": 8, "faction": "Independent"},
            {"name": "Ghost of Vega", "role": "ally", "level": 10, "faction": "Galactic Federation"},
        ]

        for npc_data in npcs:
            faction, _ = Faction.objects.get_or_create(name=npc_data["faction"], defaults={"description": "Faction description"})
            NPC.objects.create(
                name=npc_data["name"],
                role=npc_data["role"],
                level=npc_data["level"],
                faction=faction,
                dialogue=f"Hello, I am {npc_data['name']}.",
                reputation_effect=5 if npc_data["role"] in ["officer", "ally"] else -5
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded general NPCs!"))
