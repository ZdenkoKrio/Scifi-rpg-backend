from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

COMPOSITION_TYPES = [
    ("rocky", "Rocky"),
    ("gaseous", "Gaseous"),
    ("metallic", "Metallic"),
    ("ice", "Icy"),
    ("unknown", "Unknown"),
]


class CelestialBody(models.Model):
    """Abstract base model for all celestial bodies (planets, asteroids, stations)."""
    name = models.CharField(max_length=100)
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    composition = models.CharField(max_length=20, choices=COMPOSITION_TYPES, default="unknown")
    resource_richness = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Resource value (0 = barren, 100 = rich)"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"