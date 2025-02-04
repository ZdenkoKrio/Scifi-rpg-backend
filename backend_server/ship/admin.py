from django.contrib import admin
from .models import Ship, ShipArmor, ShipWeapon, ShipUpgrade, ShipCrew


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    """Admin panel for managing ships."""
    list_display = ("name", "ship_type", "owner", "hp", "max_hp", "shield", "max_shield", "speed")
    search_fields = ("name", "owner__user__username")
    list_filter = ("ship_type", "owner")


@admin.register(ShipArmor)
class ShipArmorAdmin(admin.ModelAdmin):
    """Admin panel for managing ship armor."""
    list_display = ("name", "defense_bonus", "ship")
    search_fields = ("name", "ship__name")


@admin.register(ShipWeapon)
class ShipWeaponAdmin(admin.ModelAdmin):
    """Admin panel for managing ship weapons."""
    list_display = ("name", "damage", "critical_chance", "ship")
    search_fields = ("name", "ship__name")


@admin.register(ShipUpgrade)
class ShipUpgradeAdmin(admin.ModelAdmin):
    """Admin panel for managing ship upgrades."""
    list_display = ("name", "effect", "energy_cost", "ship")
    search_fields = ("name", "ship__name")


@admin.register(ShipCrew)
class ShipCrewAdmin(admin.ModelAdmin):
    """Admin panel for managing ship crew members."""
    list_display = ("name", "role", "skill_level", "ship")
    search_fields = ("name", "ship__name")
    list_filter = ("role",)
