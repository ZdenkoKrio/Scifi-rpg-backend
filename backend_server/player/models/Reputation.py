from django.db import models
from .Player import Player
from diplomation import Faction


class Reputation(models.Model):
    """Represents a player's reputation with different factions."""
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="reputations")
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name="faction_reputations")
    value = models.IntegerField(default=0)  # Reputation can be positive or negative

    def __str__(self):
        return f"{self.player.user.username} - {self.faction.name}: {self.value}"
