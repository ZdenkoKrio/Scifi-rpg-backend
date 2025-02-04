from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Calls all diplomation-related seed commands in the correct order."""
    help = "Populate the database with all factions, species, and species-faction relationships."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding all diplomation data...")

        call_command("seed_factions")
        call_command("seed_species")
        call_command("seed_species_faction")

        self.stdout.write(self.style.SUCCESS("Successfully seeded all diplomation data!"))
