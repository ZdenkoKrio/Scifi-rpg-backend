from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Master command to run all 'seed_all_<appname>' commands and populate the database."""

    help = "Populates the database by running all seed commands for each application."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting full database seeding...\n"))

        commands = [
            "seed_all_diplomation",
            "seed_players",
            "seed_all_npcs",
            "seed_all_items",
            "seed_all_ships",
            "seed_all_space",
        ]

        for command in commands:
            self.stdout.write(self.style.NOTICE(f"Running: {command}"))
            call_command(command)

        self.stdout.write(self.style.SUCCESS("\n✅ Database seeding completed successfully!"))
