from django.db import models
from .CelestialBody import CelestialBody
from .StarSystem import StarSystem
from django.core.validators import MinValueValidator, MaxValueValidator

STAR_TYPES = [
    ("main_sequence", "Main Sequence"),
    ("red_giant", "Red Giant"),
    ("white_dwarf", "White Dwarf"),
    ("neutron", "Neutron Star"),
    ("black_hole", "Black Hole"),
]


class Star(CelestialBody):
    """Represents a star at the center of a star system."""
    star_system = models.OneToOneField(StarSystem, on_delete=models.CASCADE, related_name="star")
    star_type = models.CharField(max_length=50, choices=STAR_TYPES, default="main_sequence")
    temperature = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(50000)],
        help_text="Temperature in Kelvin"
    )
    size = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000)],
        help_text="Relative size metric"
    )
    luminosity = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(1000.0)],
        help_text="Sun = 1.0"
    )

    def __str__(self):
        return f"{self.name} ({self.star_type}) - System: {self.star_system.name}"