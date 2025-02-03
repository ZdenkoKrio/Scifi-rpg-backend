from django.db import models
from .StarSystem import StarSystem
from .CelestialBody import CelestialBody


class Star(CelestialBody):
    """Represents a star at the center of a star system."""
    name = models.CharField(max_length=100, unique=True)
    star_system = models.OneToOneField(StarSystem, on_delete=models.CASCADE, related_name="star")
    star_type = models.CharField(max_length=50, choices=[
        ("main_sequence", "Main Sequence"),
        ("red_giant", "Red Giant"),
        ("white_dwarf", "White Dwarf"),
        ("neutron", "Neutron Star"),
        ("black_hole", "Black Hole"),
    ])
    temperature = models.IntegerField()  # Kelvin
    size = models.IntegerField()  # Relative size metric
    luminosity = models.FloatField()  # Sun = 1.0

    def __str__(self):
        return f"{self.name} ({self.star_type}) - System: {self.star_system.name}"