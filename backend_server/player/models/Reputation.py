from django.db import models


class Reputation(models.Model):
    """Represents a player's reputation with different factions."""
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="reputations")
    faction = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.username} - {self.faction}: {self.value}"
