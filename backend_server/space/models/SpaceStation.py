from django.db import models
from .CelestialBody import CelestialBody

STATION_TYPES = [
    ("trading", "Trading Station"),
    ("military", "Military Base"),
    ("research", "Research Facility"),
    ("free_floating", "Independent Station"),
]


class SpaceStation(CelestialBody):
    """Represents a space station in a star system or free-floating in space."""
    station_type = models.CharField(max_length=20, choices=STATION_TYPES, default="trading")
    owner_faction = models.ForeignKey("diplomation.Faction", on_delete=models.SET_NULL, null=True, blank=True)
    orbiting_object = models.ForeignKey(
        CelestialBody, on_delete=models.SET_NULL, null=True, blank=True, related_name="orbiting_stations",
        help_text="The celestial body this station orbits (if any)."
    )
    star_system = models.ForeignKey("StarSystem", on_delete=models.CASCADE, related_name="stations")

    def __str__(self):
        if self.orbiting_object:
            return f"{self.name} (Station orbiting {self.orbiting_object.name})"
        return f"{self.name} (Independent Station in {self.star_system.name})"
