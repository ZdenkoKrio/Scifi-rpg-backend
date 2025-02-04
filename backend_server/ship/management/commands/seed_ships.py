from django.core.management.base import BaseCommand
from player.models import Player
from ship.models import Ship


class Command(BaseCommand):
    """Seeds the database with various types of spaceships."""
    help = "Populate the database with test spaceships."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with ships...")

        player1 = Player.objects.filter(user__username="TestPlayer1").first()
        player2 = Player.objects.filter(user__username="TestPlayer2").first()

        ships = [
            {"owner": player1, "name": "Starfire", "ship_type": "fighter", "hp": 1200, "shield": 600, "speed": 70},
            {"owner": player1, "name": "Titan Hauler", "ship_type": "freighter", "hp": 3000, "shield": 1000, "speed": 30},
            {"owner": player2, "name": "Nebula Explorer", "ship_type": "explorer", "hp": 1400, "shield": 800, "speed": 90},
            {"owner": player2, "name": "Dreadnought", "ship_type": "battleship", "hp": 5000, "shield": 2000, "speed": 40},
        ]

        for ship_data in ships:
            Ship.objects.create(**ship_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded ships!"))
