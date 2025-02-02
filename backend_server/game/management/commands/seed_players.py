from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from game.models.player import Player


class Command(BaseCommand):
    """Seeds the database with fully initialized test players."""
    help = "Seed the database with fully initialized test players."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with fully initialized test players...")

        user1 = User.objects.create(username="TestPlayer1")
        user2 = User.objects.create(username="TestPlayer2")

        player1 = Player.objects.create(
            user=user1,
            level=5,
            class_type="Void Ranger",
            hp=240, max_hp=300,
            energy=80, max_energy=120,
            stamina=120,
            strength=18, defense=12, agility=14,
            intelligence=10, luck=6,
            credits=500, experience=1500, next_level_exp=5000,
            fights_won=3, fights_lost=1,
            missions_completed=5, missions_failed=2
        )

        player2 = Player.objects.create(
            user=user2,
            level=3,
            class_type="Cyber Warrior",
            hp=200, max_hp=280,
            energy=70, max_energy=100,
            stamina=110,
            strength=16, defense=10, agility=12,
            intelligence=12, luck=5,
            credits=300, experience=900, next_level_exp=4000,
            fights_won=2, fights_lost=2,
            missions_completed=3, missions_failed=1
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded fully initialized test players!"))
