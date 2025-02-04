from django.core.management.base import BaseCommand
from ship.models import Ship, ShipArmor, ShipWeapon, ShipUpgrade


class Command(BaseCommand):
    """Seeds the database with ship weapons, armor, and upgrades."""
    help = "Populate the database with ship equipment."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with ship equipment...")

        ship1 = Ship.objects.filter(name="Starfire").first()
        ship2 = Ship.objects.filter(name="Titan Hauler").first()

        weapons = [
            {"ship": ship1, "name": "Plasma Cannon", "damage": 100, "critical_chance": 15.0, "energy_consumption": 10},
            {"ship": ship2, "name": "Heavy Railgun", "damage": 200, "critical_chance": 10.0, "energy_consumption": 15},
        ]

        armors = [
            {"ship": ship1, "name": "Nano Shield", "defense_bonus": 50, "special_effect": "Reduces plasma damage by 20%"},
            {"ship": ship2, "name": "Titanium Armor", "defense_bonus": 100, "special_effect": "Absorbs 10% of kinetic damage"},
        ]

        upgrades = [
            {"ship": ship1, "name": "Overclocked Engines", "effect": "Increases speed by 15%", "energy_cost": 5},
            {"ship": ship2, "name": "Advanced Shield Generator", "effect": "Boosts shields by 20%", "energy_cost": 8},
        ]

        for weapon in weapons:
            ShipWeapon.objects.create(**weapon)
        for armor in armors:
            ShipArmor.objects.create(**armor)
        for upgrade in upgrades:
            ShipUpgrade.objects.create(**upgrade)

        self.stdout.write(self.style.SUCCESS("Successfully seeded ship equipment!"))
