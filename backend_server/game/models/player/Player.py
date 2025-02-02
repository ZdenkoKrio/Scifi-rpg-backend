from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    """Represents a player's game-related attributes."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")
    level = models.IntegerField(default=1)
    class_type = models.CharField(max_length=50, default="Void Ranger")
    hp = models.IntegerField(default=240)
    max_hp = models.IntegerField(default=300)
    energy = models.IntegerField(default=80)
    max_energy = models.IntegerField(default=120)
    stamina = models.IntegerField(default=120)

    strength = models.IntegerField(default=18)
    defense = models.IntegerField(default=12)
    agility = models.IntegerField(default=14)
    intelligence = models.IntegerField(default=10)
    luck = models.IntegerField(default=6)

    credits = models.DecimalField(max_digits=12, decimal_places=2, default=250)
    experience = models.IntegerField(default=3500)
    next_level_exp = models.IntegerField(default=5000)

    equipped_weapon = models.ForeignKey("Weapon", on_delete=models.SET_NULL, null=True, blank=True)
    equipped_armor = models.ForeignKey("Armor", on_delete=models.SET_NULL, null=True, blank=True)

    fights_won = models.IntegerField(default=0)
    fights_lost = models.IntegerField(default=0)
    missions_completed = models.IntegerField(default=0)
    missions_failed = models.IntegerField(default=0)

    def calculate_critical_damage(self):
        """Calculates critical damage based on the equipped weapon and player attributes."""
        if self.equipped_weapon:
            return self.equipped_weapon.base_damage * (1 + self.equipped_weapon.critical_damage_bonus / 100)
        return 0

    def __str__(self):
        return f"{self.user.username} (Level {self.level})"