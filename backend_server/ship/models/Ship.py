from django.db import models
from player.models import Player


SHIP_TYPES = [
    ("fighter", "Fighter"),
    ("freighter", "Freighter"),
    ("explorer", "Explorer"),
    ("battleship", "Battleship"),
]


class Ship(models.Model):
    """Represents a player's spaceship with upgradeable attributes."""
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="ships")
    name = models.CharField(max_length=100, default="Unnamed Ship")
    ship_type = models.CharField(max_length=50, choices=SHIP_TYPES)

    hp = models.IntegerField(default=1000)
    max_hp = models.IntegerField(default=1000)
    shield = models.IntegerField(default=500)
    max_shield = models.IntegerField(default=500)

    speed = models.IntegerField(default=50)
    cargo_capacity = models.IntegerField(default=100)
    fuel_capacity = models.IntegerField(default=200)

    weapon_slots = models.IntegerField(default=2)
    armor_slots = models.IntegerField(default=2)
    crew_capacity = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.name} ({self.ship_type}) - Owner: {self.owner.user.username}"
