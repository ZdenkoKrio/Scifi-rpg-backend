from django.db import models


class NPC(models.Model):
    """Represents a general non-player character (NPC) in the game."""
    name = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=50, choices=[
        ("merchant", "Merchant"),
        ("bounty_hunter", "Bounty Hunter"),
        ("pirate", "Pirate"),
        ("officer", "Officer"),
        ("scientist", "Scientist"),
        ("enemy", "Enemy"),
        ("ally", "Ally"),
    ])
    level = models.IntegerField(default=1)
    faction = models.CharField(max_length=100, blank=True, null=True)  # Optional faction affiliation
    dialogue = models.TextField(blank=True)  # Stores dialogue or quest text
    reputation_effect = models.IntegerField(default=0)  # Effect on player's reputation when interacting

    def __str__(self):
        return f"{self.name} ({self.role})"