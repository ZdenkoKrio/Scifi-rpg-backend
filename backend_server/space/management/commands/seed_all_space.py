from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Runs all space-related seed commands."""
    help = "Seeds the entire galaxy with star systems, celestial bodies, and space phenomena."

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Seeding the galaxy with space objects...")

        call_command("seed_star_systems")
        call_command("seed_stars")
        call_command("seed_planets")
        call_command("seed_moons")
        call_command("seed_asteroids")
        call_command("seed_nebulas")
        call_command("seed_space_stations")
        call_command("seed_unknown_objects")

        self.stdout.write(self.style.SUCCESS("🌌 ✅ Galaxy successfully populated with celestial objects!"))
