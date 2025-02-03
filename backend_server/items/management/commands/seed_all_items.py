from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Runs all seed commands to populate the database."""
    help = "Runs all seed commands in the correct order."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding entire database...")

        call_command("seed_weapons")
        call_command("seed_armors")
        call_command("seed_jewelry")
        call_command("seed_quest_items")

        self.stdout.write(self.style.SUCCESS("Database for items app seeding complete!"))
