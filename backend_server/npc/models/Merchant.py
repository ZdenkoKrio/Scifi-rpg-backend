from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .NPC import NPC


class Merchant(models.Model):
    """Represents an NPC merchant who sells items."""
    npc = models.OneToOneField("NPC", on_delete=models.CASCADE, related_name="merchant")

    def __str__(self):
        return f"{self.npc.name} (Merchant)"


class MerchantInventory(models.Model):
    """Tracks the stock of items a merchant has."""

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="stock")

    # GenericForeignKey to support multiple item types
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")

    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.merchant.npc.name} sells {self.quantity}x {self.item} for {self.price} credits"
