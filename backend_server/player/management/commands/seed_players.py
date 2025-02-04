from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from player import Player, PlayerItem, Reputation, Resistance, Skill
from items import Item
from diplomation import Faction


class Command(BaseCommand):
    """Seeds the database with test players, inventory, reputation, resistances, and skills."""
    help = "Populate the database with test players and related data."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with test players...")

        user1 = User.objects.create_user(username="TestPlayer1", password="password123")
        user2 = User.objects.create_user(username="TestPlayer2", password="password123")
        user3 = User.objects.create_user(username="TestPlayer3", password="password123")

        player1 = Player.objects.create(user=user1, level=5, class_type="cyber_warrior", credits=1000, experience=2500)
        player2 = Player.objects.create(user=user2, level=3, class_type="pilot", credits=750, experience=1500)
        player3 = Player.objects.create(user=user3, level=7, class_type="hacker", credits=2000, experience=4000)

        medkit = Item.objects.create(name="MedKit", item_type="consumable", description="Restores 50 HP", value=100)
        shield_booster = Item.objects.create(name="Shield Booster", item_type="misc", description="Increases shield capacity by 20%", value=200)

        PlayerItem.objects.create(player=player1, item=medkit, quantity=3, is_equipped=False)
        PlayerItem.objects.create(player=player2, item=shield_booster, quantity=2, is_equipped=False)
        PlayerItem.objects.create(player=player3, item=medkit, quantity=1, is_equipped=False)
#TODO upravi k existujucim frakciam
        federation, _ = Faction.objects.get_or_create(name="Galactic Federation", description="A union of planets.")
        pirates, _ = Faction.objects.get_or_create(name="Void Pirates", description="A group of space bandits.")

        Reputation.objects.create(player=player1, faction=federation, value=50)
        Reputation.objects.create(player=player1, faction=pirates, value=-10)
        Reputation.objects.create(player=player2, faction=federation, value=20)
        Reputation.objects.create(player=player2, faction=pirates, value=30)

        Resistance.objects.create(player=player1, type="plasma", value=15)
        Resistance.objects.create(player=player1, type="EMP", value=10)
        Resistance.objects.create(player=player2, type="radiation", value=20)
        Resistance.objects.create(player=player2, type="plasma", value=5)
#TODO vytvorit pevny zoznam skills, hraci ich maju len priradene
        skill1, _ = Skill.objects.get_or_create(name="Overcharge", effect="Boosts damage by 50% for 10s", cooldown=15)
        skill2, _ = Skill.objects.get_or_create(name="Defensive Mode", effect="Reduces incoming damage by 30%", cooldown=20)

        self.stdout.write(self.style.SUCCESS("Successfully seeded database with test players!"))
