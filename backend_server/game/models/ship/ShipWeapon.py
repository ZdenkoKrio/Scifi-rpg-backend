from django.db import models
from .Ship import Ship


class ShipWeapon(models.Model):
    """Represents weapons mounted on a spaceship."""
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name="weapons")
    name = models.CharField(max_length=100)
    damage = models.IntegerField(default=50)
    critical_chance = models.FloatField(default=10.0)
    energy_consumption = models.IntegerField(default=5)  # Energy cost per shot

    def __str__(self):
        return f"{self.name} (DMG: {self.damage}) - {self.ship.name}"
