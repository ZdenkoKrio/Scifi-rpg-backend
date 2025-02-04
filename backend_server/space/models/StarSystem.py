from django.db import models
from diplomation import Faction


class StarSystem(models.Model):
    """Represents a star system in the galaxy."""
    name = models.CharField(max_length=100, unique=True)
    faction = models.ForeignKey(Faction, on_delete=models.SET_NULL, null=True, blank=True, related_name="systems")
    coordinates_x = models.FloatField()
    coordinates_y = models.FloatField()
    coordinates_z = models.FloatField()

    def __str__(self):
        return f"{self.name} - Controlled by {self.faction.name if self.faction else 'No Faction'}"