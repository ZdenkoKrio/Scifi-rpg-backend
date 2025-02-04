from django.db import models


DAMAGE_TYPES = [
        ("plasma", "Plasma"),
        ("EMP", "EMP"),
        ("radiation", "Radiation"),
    ]


class Resistance(models.Model):
    """Represents a player's resistance to different types of damage."""
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="resistances")
    type = models.CharField(max_length=50, choices=DAMAGE_TYPES)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.user.username} - {self.get_type_display()}: {self.value}"
