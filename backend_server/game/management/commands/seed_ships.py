from django.core.management.base import BaseCommand
from game.models.player import Player
from game.models.ship import Ship, ShipWeapon, ShipArmor, ShipUpgrade, ShipCrew
from game.models.npc import NPC


class Command(BaseCommand):
    """Seeds the database with test spaceships and crew."""
    help = "Seed the database with test spaceships and crew."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with player ships and crew...")

        # Fetch players
        player1 = Player.objects.get(user__username="TestPlayer1")
        player2 = Player.objects.get(user__username="TestPlayer2")

        # Create ships
        ship1 = Ship.objects.create(owner=player1, name="Star Fury", ship_type="fighter", hp=1200, shield=600, cargo_capacity=50)
        ship2 = Ship.objects.create(owner=player2, name="Nebula Trader", ship_type="freighter", hp=2000, shield=1000, cargo_capacity=200)

        # Create weapons
        ShipWeapon.objects.create(ship=ship1, name="Plasma Cannons", damage=100, critical_chance=20, energy_consumption=10)
        ShipWeapon.objects.create(ship=ship2, name="Ion Blaster", damage=80, critical_chance=15, energy_consumption=8)

        # Create armor
        ShipArmor.objects.create(ship=ship1, name="Reactive Shields", defense_bonus=50, special_effect="Absorbs 10% plasma damage")
        ShipArmor.objects.create(ship=ship2, name="Heavy Plating", defense_bonus=80, special_effect="Reduces kinetic damage")

        # Create ship upgrades
        ShipUpgrade.objects.create(ship=ship1, name="Afterburner", effect="Increases speed by 30%", energy_cost=15)
        ShipUpgrade.objects.create(ship=ship2, name="Cargo Expansion", effect="Increases cargo hold by 50", energy_cost=5)

        # Create crew members (using NPCs)
        pilot_npc = NPC.objects.get(name="Captain Raze")
        engineer_npc = NPC.objects.get(name="Doctor Yara")

        ShipCrew.objects.create(ship=ship1, npc=pilot_npc, name=pilot_npc.name, role="pilot", skill_level=3)
        ShipCrew.objects.create(ship=ship2, npc=engineer_npc, name=engineer_npc.name, role="engineer", skill_level=5)

        self.stdout.write(self.style.SUCCESS("Successfully seeded ships and crew!"))
