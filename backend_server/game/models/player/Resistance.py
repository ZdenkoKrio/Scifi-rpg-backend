from django.db import models


class Resistance(models.Model):
    """Represents a player's resistance to different types of damage."""
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="resistances")
    type = models.CharField(max_length=50, choices=[
        ("plasma", "Plasma"),
        ("EMP", "EMP"),
        ("radiation", "Radiation"),
    ])
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.username} - {self.type}: {self.value}"
