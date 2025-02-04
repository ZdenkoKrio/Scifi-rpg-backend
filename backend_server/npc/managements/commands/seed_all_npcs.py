from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Calls all NPC-related seed commands in the correct order."""
    help = "Populate the database with all NPCs (General NPCs, Quest Givers, and Merchants)."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding all NPCs...")

        call_command("seed_general_npcs")
        call_command("seed_quest_givers")
        call_command("seed_merchants")

        self.stdout.write(self.style.SUCCESS("Successfully seeded all NPCs!"))
