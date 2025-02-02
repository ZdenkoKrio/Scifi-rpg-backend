from django.db import models


class ShipCrew(models.Model):
    """Represents crew members assigned to a spaceship."""
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE, related_name="crew")
    npc = models.ForeignKey("NPC", on_delete=models.SET_NULL, null=True, blank=True, related_name="crew_member")  # Optional link to NPC
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[
        ("pilot", "Pilot"),
        ("engineer", "Engineer"),
        ("gunner", "Gunner"),
        ("medic", "Medic"),
        ("scientist", "Scientist"),
    ])
    skill_level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.role}) - {self.ship.name}"
