from django.db import models
from .CelestialBody import CelestialBody
from game.models.diplomation import Faction


class SpaceStation(CelestialBody):
    """Represents a space station in a star system."""
    station_type = models.CharField(max_length=100, choices=[
        ("trading", "Trading Station"),
        ("military", "Military Base"),
        ("research", "Research Facility"),
    ])
    owner_faction = models.ForeignKey(Faction, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Space Station) - {self.star_system.name}"
