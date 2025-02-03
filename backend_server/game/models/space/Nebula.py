from django.db import models
from .StarSystem import StarSystem
from .CelestialBody import CelestialBody


class Nebula(CelestialBody):
    """Represents a nebula in space, which may contain resources or dangers."""
    name = models.CharField(max_length=100, unique=True)
    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, related_name="nebulas")
    size = models.IntegerField(default=500)  # General size metric
    gas_composition = models.CharField(max_length=100, choices=[
        ("hydrogen", "Hydrogen-Rich"),
        ("ionized", "Ionized Plasma"),
        ("radioactive", "Radioactive"),
        ("unknown", "Unknown Composition"),
    ])
    visibility = models.IntegerField(default=50)  # How difficult it is to navigate (0-100)
    resource_richness = models.IntegerField(default=0)  # 0 = barren, 100 = rich
    has_storms = models.BooleanField(default=False)  # If true, traveling through is dangerous

    def __str__(self):
        return f"{self.name} (Nebula) - {self.star_system.name}"