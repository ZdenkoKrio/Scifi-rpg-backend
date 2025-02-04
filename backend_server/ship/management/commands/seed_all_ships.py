from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Calls all ship-related seed commands in the correct order."""
    help = "Populate the database with all ships and related data."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding all ship data...")

        call_command("seed_ships")
        call_command("seed_ship_equipment")
        call_command("seed_ship_crew")

        self.stdout.write(self.style.SUCCESS("Successfully seeded all ship-related data!"))
