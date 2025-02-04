from django.core.management.base import BaseCommand
from items.models import Armor


class Command(BaseCommand):
    """Seeds the database with a set of predefined armors."""
    help = "Seed the database with armors."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding armors...")

        armors = [
            {"name": "Titanium Battle Suit", "rarity": "epic", "defense_bonus": 40, "special_effect": "Absorbs 15% plasma damage"},
            {"name": "Stealth Cloak", "rarity": "rare", "defense_bonus": 15, "special_effect": "Reduces detection by 50%"},
            {"name": "Nano Fiber Vest", "rarity": "uncommon", "defense_bonus": 25, "special_effect": "Provides minor radiation resistance"},
            {"name": "Void Shield", "rarity": "legendary", "defense_bonus": 60, "special_effect": "Nullifies EMP attacks"},
            {"name": "Gravity Armor", "rarity": "epic", "defense_bonus": 50, "special_effect": "Reduces knockback effects"},
            {"name": "Neutronium Plating", "rarity": "rare", "defense_bonus": 45, "special_effect": "Reduces laser damage"},
            {"name": "Chameleon Suit", "rarity": "uncommon", "defense_bonus": 20, "special_effect": "Boosts stealth by 30%"},
            {"name": "Warp Shield", "rarity": "legendary", "defense_bonus": 65, "special_effect": "Reflects 10% of incoming damage"},
            {"name": "Cybernetic Chestplate", "rarity": "epic", "defense_bonus": 55, "special_effect": "Increases energy regeneration"},
            {"name": "Thermal Guard", "rarity": "rare", "defense_bonus": 38, "special_effect": "Immune to fire damage"},
            {"name": "Phase Vest", "rarity": "common", "defense_bonus": 10, "special_effect": "Slightly increases speed"},
            {"name": "Quantum Barrier", "rarity": "legendary", "defense_bonus": 70, "special_effect": "Nullifies damage under 10 HP"},
            {"name": "Tachyon Plate", "rarity": "epic", "defense_bonus": 48, "special_effect": "Halves cooldowns for abilities"},
            {"name": "Cryo Vest", "rarity": "rare", "defense_bonus": 32, "special_effect": "Immune to cold damage"},
            {"name": "Chrono Cloak", "rarity": "legendary", "defense_bonus": 66, "special_effect": "Grants time warp ability"},
            {"name": "Exo Suit", "rarity": "uncommon", "defense_bonus": 30, "special_effect": "Increases stamina by 15%"},
            {"name": "AI-Enhanced Armor", "rarity": "epic", "defense_bonus": 52, "special_effect": "Autorepairs over time"},
            {"name": "Black Hole Shield", "rarity": "legendary", "defense_bonus": 75, "special_effect": "Absorbs energy damage"},
            {"name": "Neural Augment Vest", "rarity": "uncommon", "defense_bonus": 28, "special_effect": "Boosts intelligence"},
            {"name": "Solar Absorber", "rarity": "rare", "defense_bonus": 35, "special_effect": "Absorbs sunlight for shield regeneration"},
        ]

        for armor_data in armors:
            Armor.objects.get_or_create(**armor_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded armors!"))
