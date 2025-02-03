from django.db import models
from .Item import Item


class Jewelry(Item):
    """Represents a rare or valuable item with no combat use."""
    origin = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Rarity: {self.rarity}) - Origin: {self.origin or 'Unknown'}"
