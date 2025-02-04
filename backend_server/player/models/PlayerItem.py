from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PlayerItem(models.Model):
    """Represents an item in a player's inventory, tracking quantity and equipped status."""
    player = models.ForeignKey("player.Player", on_delete=models.CASCADE, related_name="inventory")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")

    quantity = models.IntegerField(default=1)
    is_equipped = models.BooleanField(default=False)

    def __str__(self):
        status = " (Equipped)" if self.is_equipped else ""
        return f"{self.player.user.username} owns {self.quantity}x {self.item}{status}"
