from django.core.management.base import BaseCommand
from ship import Ship, ShipCrew


class Command(BaseCommand):
    """Seeds the database with ship crew members."""
    help = "Populate the database with ship crew members."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with ship crew...")

        ship1 = Ship.objects.filter(name="Starfire").first()
        ship2 = Ship.objects.filter(name="Titan Hauler").first()

        crew_members = [
            {"ship": ship1, "name": "John Shepard", "role": "pilot", "skill_level": 5},
            {"ship": ship1, "name": "Tali'Zorah", "role": "engineer", "skill_level": 4},
            {"ship": ship2, "name": "Garrus Vakarian", "role": "gunner", "skill_level": 5},
            {"ship": ship2, "name": "Mordin Solus", "role": "scientist", "skill_level": 5},
        ]

        for crew in crew_members:
            ShipCrew.objects.create(**crew)

        self.stdout.write(self.style.SUCCESS("Successfully seeded ship crew!"))
        