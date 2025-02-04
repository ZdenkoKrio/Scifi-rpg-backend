from django.db import models


class PlayerItem(models.Model):
    """Represents an item in a player's inventory, tracking quantity and equipped status."""
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="inventory")
    item = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_equipped = models.BooleanField(default=False)

    def __str__(self):
        status = " (Equipped)" if self.is_equipped else ""
        return f"{self.player.user.username} owns {self.quantity}x {self.item.name}{status}"
