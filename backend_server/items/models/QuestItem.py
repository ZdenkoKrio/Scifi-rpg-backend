from django.db import models
from .Item import Item


class QuestItem(Item):
    """Represents a mission-related item that cannot be sold or used outside of a quest."""
    quest_name = models.CharField(max_length=200)
    is_consumed = models.BooleanField(default=False)  # if item is discard after mission accomplice

    def __str__(self):
        status = " (Consumed after use)" if self.is_consumed else ""
        return f"{self.name} (Quest: {self.quest_name}) - {self.rarity}{status}"
