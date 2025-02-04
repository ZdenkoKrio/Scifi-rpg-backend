from django.db import models
from .CelestialBody import CelestialBody
from .StarSystem import StarSystem
from django.core.validators import MinValueValidator, MaxValueValidator

UNKNOWN_OBJECT_TYPES = [
    ("black_hole", "Black Hole"),
    ("anomaly", "Anomaly"),
    ("derelict_station", "Derelict Station"),
    ("alien_artifact", "Alien Artifact"),
    ("wormhole", "Wormhole"),
]


class UnknownObject(CelestialBody):
    """Represents an unknown or mysterious object in space."""
    object_type = models.CharField(max_length=50, choices=UNKNOWN_OBJECT_TYPES, default="anomaly")
    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, null=True, blank=True, related_name="unknown_objects")
    coordinates_x = models.FloatField(null=True, blank=True, help_text="X position in the galaxy (if outside a system).")
    coordinates_y = models.FloatField(null=True, blank=True, help_text="Y position in the galaxy (if outside a system).")
    coordinates_z = models.FloatField(null=True, blank=True, help_text="Z position in the galaxy (if outside a system).")
    danger_level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="0 = safe, 100 = extreme danger"
    )
    scientific_value = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Worth for research (0-100)"
    )
    can_interact = models.BooleanField(default=True, help_text="Can players interact with it?")

    def __str__(self):
        if self.star_system:
            return f"{self.name} ({self.object_type}) in {self.star_system.name}"
        return f"{self.name} ({self.object_type}) at [{self.coordinates_x}, {self.coordinates_y}, {self.coordinates_z}]"