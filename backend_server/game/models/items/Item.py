from django.db import models


class Item(models.Model):
    """Represents an item in the player's inventory."""
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50, choices=[
        ("weapon", "Weapon"),
        ("armor", "Armor"),
        ("consumable", "Consumable"),
        ("misc", "Miscellaneous"),
    ])
    description = models.TextField(blank=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name
