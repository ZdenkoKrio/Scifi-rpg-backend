from django.db import models


class QuestGiver(models.Model):
    """Represents an NPC that gives quests to players."""
    npc = models.OneToOneField("NPC", on_delete=models.CASCADE, related_name="quest_giver")
    available_quests = models.ManyToManyField("items.QuestItem", related_name="quest_givers")

    def __str__(self):
        return f"{self.npc.name} (Quest Giver)"
