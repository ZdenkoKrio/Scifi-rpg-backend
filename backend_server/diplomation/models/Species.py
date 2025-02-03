from django.db import models
from game.models import Planet


class Species(models.Model):
    """Represents a sentient or non-sentient species in the galaxy."""
    name = models.CharField(max_length=100, unique=True)
    species_type = models.CharField(max_length=50, choices=[
        ("intelligent", "Intelligent"),
        ("primitive", "Primitive"),
        ("animal", "Animal"),
        ("synthetic", "Synthetic AI"),
    ])
    homeworld = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, blank=True, related_name="inhabitants")
    lifespan = models.IntegerField(default=100)  # Average lifespan in years
    average_height = models.FloatField(default=1.8)  # Meters
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.species_type}) - Homeworld: {self.homeworld.name if self.homeworld else 'Unknown'}"
