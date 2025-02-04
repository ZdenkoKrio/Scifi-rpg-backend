from django.db import models
from .CelestialBody import CelestialBody
from django.core.validators import MinValueValidator


ATMOSPHERE_TYPES = [
    ("breathable", "Breathable"),
    ("toxic", "Toxic"),
    ("none", "No Atmosphere"),
]

ECONOMY_TYPES = [
    ("trade_hub", "Trade Hub"),
    ("industrial", "Industrial"),
    ("agriculture", "Agriculture"),
    ("military", "Military Base"),
]


class Planet(CelestialBody):
    """Represents a planet within a star system."""
    star_system = models.ForeignKey("StarSystem", on_delete=models.CASCADE, related_name="planets")
    atmosphere_type = models.CharField(max_length=20, choices=ATMOSPHERE_TYPES, default="none")
    population = models.BigIntegerField(default=0, validators=[MinValueValidator(0)])
    economy_type = models.CharField(max_length=20, choices=ECONOMY_TYPES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Planet in {self.star_system.name})"
