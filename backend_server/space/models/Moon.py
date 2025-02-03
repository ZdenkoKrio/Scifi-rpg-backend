from django.db import models
from .Planet import Planet
from .CelestialBody import CelestialBody


class Moon(CelestialBody):
    """Represents a moon orbiting a planet."""
    name = models.CharField(max_length=100, unique=True)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="moons")
    size = models.IntegerField(default=10)  # General size metric
    atmosphere_type = models.CharField(max_length=100, choices=[
        ("breathable", "Breathable"),
        ("toxic", "Toxic"),
        ("none", "No Atmosphere"),
    ])
    has_mining_colony = models.BooleanField(default=False)  # Whether mining is possible
    has_military_base = models.BooleanField(default=False)  # Whether there is a military base
    population = models.IntegerField(default=0)  # Inhabitants (if any)

    def __str__(self):
        return f"{self.name} (Moon of {self.planet.name})"