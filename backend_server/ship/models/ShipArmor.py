from django.db import models


class ShipArmor(models.Model):
    """Represents defensive armor on a spaceship."""
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE, related_name="armor")
    name = models.CharField(max_length=100)
    defense_bonus = models.IntegerField(default=20)
    special_effect = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (+{self.defense_bonus} DEF) - {self.ship.name}"