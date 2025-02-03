from django.db import models
from .CelestialBody import CelestialBody


class Asteroid(CelestialBody):
    """Represents an asteroid in a star system."""
    is_mining_site = models.BooleanField(default=False)
    has_pirate_activity = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Asteroid) - {self.star_system.name}"
