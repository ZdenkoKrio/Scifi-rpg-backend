from django.db import models


ITEM_RARITIES = [
    ("common", "Common"),
    ("uncommon", "Uncommon"),
    ("rare", "Rare"),
    ("epic", "Epic"),
    ("legendary", "Legendary"),
]


class Item(models.Model):
    """Abstract model representing a generic item in the game."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    value = models.IntegerField(default=0)

    rarity = models.CharField(max_length=20, choices=ITEM_RARITIES, default="common")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.rarity})"
