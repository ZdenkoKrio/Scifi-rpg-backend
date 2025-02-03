from django.db import models
from .CelestialBody import CelestialBody


class Planet(CelestialBody):
    """Represents a planet within a star system."""
    atmosphere_type = models.CharField(max_length=100, choices=[
        ("breathable", "Breathable"),
        ("toxic", "Toxic"),
        ("none", "No Atmosphere"),
    ])
    population = models.BigIntegerField(default=0)
    economy_type = models.CharField(max_length=100, choices=[
        ("trade_hub", "Trade Hub"),
        ("industrial", "Industrial"),
        ("agriculture", "Agriculture"),
        ("military", "Military Base"),
    ], blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Planet) - {self.star_system.name}"
