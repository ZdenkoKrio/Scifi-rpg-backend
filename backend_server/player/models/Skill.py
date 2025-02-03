from django.db import models


class Skill(models.Model):
    """Represents a skill a player can use."""
    name = models.CharField(max_length=100)
    effect = models.TextField()
    cooldown = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.name} - {self.effect} (CD: {self.cooldown}s)"
    