from django.core.management.base import BaseCommand
from game.models.items import Weapon, Armor, Item
from game.models.player import PlayerItem
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Seeds the database with predefined weapons, armors, and items."""
    help = "Seed database with weapons, armor, and general items."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with items...")

        weapons = [
            {"name": "Laser Rifle", "base_damage": 70, "critical_chance": 15, "critical_damage_bonus": 50, "item_type": "weapon"},
            {"name": "Plasma Blade", "base_damage": 90, "critical_chance": 20, "critical_damage_bonus": 75, "item_type": "weapon"},
        ]

        armors = [
            {"name": "Nano Suit", "defense_bonus": 25, "special_effect": "Reduces EMP damage by 20%", "item_type": "armor"},
            {"name": "Titanium Shield", "defense_bonus": 40, "special_effect": "Blocks 10% of physical damage", "item_type": "armor"},
        ]

        items = [
            {"name": "MedKit", "item_type": "consumable", "description": "Restores 50 HP", "value": 100},
            {"name": "Shield Booster", "item_type": "misc", "description": "Increases shield capacity by 20%", "value": 200},
        ]

        for weapon in weapons:
            Weapon.objects.create(**weapon)

        for armor in armors:
            Armor.objects.create(**armor)

        for item in items:
            Item.objects.create(**item)

        user = User.objects.create(username="TestPlayer")

        laser_rifle = Weapon.objects.get(name="Laser Rifle")
        nano_suit = Armor.objects.get(name="Nano Suit")

        PlayerItem.objects.create(player=user, item=laser_rifle, quantity=1, is_equipped=True)
        PlayerItem.objects.create(player=user, item=nano_suit, quantity=1, is_equipped=True)

        self.stdout.write(self.style.SUCCESS("Successfully seeded database!"))
