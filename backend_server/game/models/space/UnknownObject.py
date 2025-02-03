from django.db import models
from .CelestialBody import CelestialBody
from StarSystem import StarSystem


class UnknownObject(CelestialBody):
    """Represents an unknown or mysterious object in space."""
    name = models.CharField(max_length=100, unique=True)
    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, related_name="unknown_objects")
    object_type = models.CharField(max_length=50, choices=[
        ("black_hole", "Black Hole"),
        ("anomaly", "Anomaly"),
        ("derelict_station", "Derelict Station"),
        ("alien_artifact", "Alien Artifact"),
        ("wormhole", "Wormhole"),
    ])
    danger_level = models.IntegerField(default=0)  # 0 = safe, 100 = extreme danger
    scientific_value = models.IntegerField(default=50)  # Worth for research (0-100)
    can_interact = models.BooleanField(default=True)  # Can players interact with it?

    def __str__(self):
        return f"{self.name} ({self.object_type}) - {self.star_system.name}"
