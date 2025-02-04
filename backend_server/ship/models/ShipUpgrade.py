from django.db import models


class ShipUpgrade(models.Model):
    """Represents installed upgrades on a spaceship."""
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE, related_name="upgrades")
    name = models.CharField(max_length=100)
    effect = models.TextField()
    energy_cost = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.name} - {self.ship.name}"