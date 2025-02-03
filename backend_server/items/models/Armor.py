from django.db import models
from .Item import Item


class Armor(Item):
    """Represents armor worn by the player."""
    defense_bonus = models.IntegerField(default=10)
    special_effect = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (+{self.defense_bonus} DEF)"
