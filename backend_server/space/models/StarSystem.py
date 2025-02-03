from django.db import models
from .CelestialBody import CelestialBody
from ..diplomation import Faction

class StarSystem(CelestialBody):
    """Represents a star system in the galaxy."""
    name = models.CharField(max_length=100, unique=True)
    faction = models.ForeignKey(Faction, on_delete=models.SET_NULL, null=True, blank=True, related_name="systems")
    coordinates_x = models.IntegerField()
    coordinates_y = models.IntegerField()
    coordinates_z = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.faction.name if self.faction else 'Unclaimed'}"