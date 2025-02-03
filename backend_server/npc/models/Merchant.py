from django.db import models
from .NPC import NPC
from items.models import Item


class Merchant(models.Model):
    """Represents an NPC merchant who sells items."""
    npc = models.OneToOneField(NPC, on_delete=models.CASCADE, related_name="merchant")
    inventory = models.ManyToManyField(Item, through="MerchantInventory")

    def __str__(self):
        return f"{self.npc.name} (Merchant)"


class MerchantInventory(models.Model):
    """Tracks the stock of items a merchant has."""
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="stock")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.merchant.npc.name} sells {self.quantity}x {self.item.name} for {self.price} credits"
    