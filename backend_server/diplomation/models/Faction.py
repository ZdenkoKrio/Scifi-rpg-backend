from django.db import models
from space import StarSystem


class Faction(models.Model):
    """Represents a faction in the galaxy with allies, enemies, and territorial control."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    capital_system = models.ForeignKey(StarSystem, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name="capital_of")

    allies = models.ManyToManyField("self", blank=True, symmetrical=True)
    enemies = models.ManyToManyField("self", blank=True, symmetrical=True)
    controlled_systems = models.ManyToManyField(StarSystem, blank=True, related_name="controlled_by")

    def __str__(self):
        return self.name
