from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

STATION_TYPES = [
    ("trading", "Trading Station"),
    ("military", "Military Base"),
    ("research", "Research Facility"),
    ("free_floating", "Independent Station"),
]


class SpaceStation(models.Model):
    """Represents a space station in a star system or free-floating in space."""
    name = models.CharField(max_length=100, unique=True)
    station_type = models.CharField(max_length=20, choices=STATION_TYPES, default="trading")
    owner_faction = models.ForeignKey("diplomation.Faction", on_delete=models.SET_NULL, null=True, blank=True)
    orbiting_content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    orbiting_object_id = models.PositiveIntegerField(null=True, blank=True)
    orbiting_object = GenericForeignKey("orbiting_content_type", "orbiting_object_id")

    star_system = models.ForeignKey(
        "space.StarSystem", on_delete=models.SET_NULL, null=True, blank=True, related_name="stations",
        help_text="The star system this station is located in (if any)."
    )

    def __str__(self):
        if self.orbiting_object:
            return f"{self.name} (Station orbiting {self.orbiting_object})"
        if self.star_system:
            return f"{self.name} (Station in {self.star_system.name})"
        return f"{self.name} (Free-floating Station)"
