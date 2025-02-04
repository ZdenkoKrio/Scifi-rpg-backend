from django.db import models
from .CelestialBody import CelestialBody
from .Planet import Planet, ATMOSPHERE_TYPES


class Moon(CelestialBody):
    """Represents a moon orbiting a planet."""
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="moons")
    atmosphere_type = models.CharField(max_length=20, choices=ATMOSPHERE_TYPES, default="none")
    has_mining_colony = models.BooleanField(default=False)
    has_military_base = models.BooleanField(default=False)
    population = models.IntegerField(default=0)

    @property
    def star_system(self):
        """Returns the star system the moon belongs to (via its planet)."""
        return self.planet.star_system

    def __str__(self):
        return f"{self.name} (Moon of {self.planet.name} in {self.star_system.name})"