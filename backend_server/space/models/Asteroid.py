from django.db import models
from .CelestialBody import CelestialBody
from .StarSystem import StarSystem


class Asteroid(CelestialBody):
    """Represents an asteroid in a star system."""
    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, related_name="asteroids")
    is_mining_site = models.BooleanField(default=False)
    has_pirate_activity = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Asteroid in {self.star_system.name})"