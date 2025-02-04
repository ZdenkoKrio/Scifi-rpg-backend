from django.core.management.base import BaseCommand
from items.models import Weapon


class Command(BaseCommand):
    """Seeds the database with a set of predefined weapons."""
    help = "Seed the database with weapons."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding weapons...")

        weapons = [
            {"name": "Plasma Rifle", "rarity": "rare", "base_damage": 75, "critical_chance": 12.5, "critical_damage_bonus": 60},
            {"name": "Energy Sword", "rarity": "epic", "base_damage": 90, "critical_chance": 18, "critical_damage_bonus": 80},
            {"name": "Ion Blaster", "rarity": "uncommon", "base_damage": 50, "critical_chance": 10, "critical_damage_bonus": 40},
            {"name": "Gauss Rifle", "rarity": "legendary", "base_damage": 120, "critical_chance": 20, "critical_damage_bonus": 90},
            {"name": "Fusion Pistol", "rarity": "common", "base_damage": 30, "critical_chance": 5, "critical_damage_bonus": 20},
            {"name": "Railgun", "rarity": "epic", "base_damage": 110, "critical_chance": 22, "critical_damage_bonus": 95},
            {"name": "Tachyon Bow", "rarity": "rare", "base_damage": 70, "critical_chance": 15, "critical_damage_bonus": 55},
            {"name": "Neutron Dagger", "rarity": "uncommon", "base_damage": 45, "critical_chance": 12, "critical_damage_bonus": 35},
            {"name": "Tesla Coil Gun", "rarity": "legendary", "base_damage": 140, "critical_chance": 25, "critical_damage_bonus": 100},
            {"name": "Graviton Lance", "rarity": "epic", "base_damage": 100, "critical_chance": 20, "critical_damage_bonus": 85},
            {"name": "Void Cannon", "rarity": "rare", "base_damage": 85, "critical_chance": 17, "critical_damage_bonus": 65},
            {"name": "Singularity Rifle", "rarity": "uncommon", "base_damage": 55, "critical_chance": 10, "critical_damage_bonus": 45},
            {"name": "Particle Accelerator", "rarity": "epic", "base_damage": 115, "critical_chance": 19, "critical_damage_bonus": 90},
            {"name": "Warp Blade", "rarity": "legendary", "base_damage": 130, "critical_chance": 23, "critical_damage_bonus": 100},
            {"name": "Phase Shifter", "rarity": "rare", "base_damage": 78, "critical_chance": 14, "critical_damage_bonus": 60},
            {"name": "Chrono Lance", "rarity": "common", "base_damage": 40, "critical_chance": 8, "critical_damage_bonus": 30},
            {"name": "Dark Matter Gauntlet", "rarity": "epic", "base_damage": 105, "critical_chance": 18, "critical_damage_bonus": 85},
            {"name": "Plasma Katana", "rarity": "legendary", "base_damage": 125, "critical_chance": 22, "critical_damage_bonus": 100},
            {"name": "Antimatter Pistol", "rarity": "uncommon", "base_damage": 48, "critical_chance": 10, "critical_damage_bonus": 38},
        ]

        for weapon_data in weapons:
            Weapon.objects.get_or_create(**weapon_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded weapons!"))
