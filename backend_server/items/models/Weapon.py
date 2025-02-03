from django.db import models
from .Item import Item


class Weapon(Item):
    """Represents a weapon with critical hit capabilities."""
    base_damage = models.IntegerField(default=50)
    critical_chance = models.FloatField(default=10.0)
    critical_damage_bonus = models.FloatField(default=50.0)

    def __str__(self):
        return f"{self.name} (DMG: {self.base_damage}, Crit: {self.critical_damage_bonus}%)"
