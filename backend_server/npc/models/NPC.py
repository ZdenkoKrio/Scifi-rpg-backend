from django.db import models
from diplomation.models import Faction

ROLE_CHOICES = [
        ("merchant", "Merchant"),
        ("bounty_hunter", "Bounty Hunter"),
        ("pirate", "Pirate"),
        ("officer", "Officer"),
        ("scientist", "Scientist"),
        ("enemy", "Enemy"),
        ("ally", "Ally"),
    ]


class NPC(models.Model):
    """Represents a general non-player character (NPC) in the game."""
    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    level = models.IntegerField(default=1)
    faction = models.ForeignKey(Faction, on_delete=models.SET_NULL, null=True, blank=True, related_name="npcs")
    dialogue = models.TextField(blank=True)
    reputation_effect = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"
    