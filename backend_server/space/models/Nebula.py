from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GAS_COMPOSITIONS = [
    ("hydrogen", "Hydrogen-Rich"),
    ("ionized", "Ionized Plasma"),
    ("radioactive", "Radioactive"),
    ("unknown", "Unknown Composition"),
]


class Nebula(models.Model):
    """Represents a nebula in space, which may contain resources or dangers."""
    name = models.CharField(max_length=100, unique=True)
    coordinates_x = models.IntegerField()
    coordinates_y = models.IntegerField()
    coordinates_z = models.IntegerField()
    gas_composition = models.CharField(max_length=20, choices=GAS_COMPOSITIONS, default="unknown")
    visibility = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="0 = completely opaque, 100 = fully visible"
    )
    has_storms = models.BooleanField(default=False, help_text="If true, traveling through is dangerous.")

    def __str__(self):
        return f"{self.name} (Nebula at {self.coordinates_x}, {self.coordinates_y}, {self.coordinates_z})"