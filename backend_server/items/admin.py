from django.contrib import admin
from .models import Weapon, Armor, Jewelry, QuestItem


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    """Admin panel for weapons."""
    list_display = ("name", "rarity", "base_damage", "critical_chance", "critical_damage_bonus")
    search_fields = ("name", "rarity")
    list_filter = ("rarity",)


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    """Admin panel for armors."""
    list_display = ("name", "rarity", "defense_bonus", "special_effect")
    search_fields = ("name", "rarity")
    list_filter = ("rarity",)


@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    """Admin panel for jewelry."""
    list_display = ("name", "rarity", "origin")
    search_fields = ("name", "rarity", "origin")
    list_filter = ("rarity",)


@admin.register(QuestItem)
class QuestItemAdmin(admin.ModelAdmin):
    """Admin panel for quest items."""
    list_display = ("name", "rarity", "quest_name", "is_consumed")
    search_fields = ("name", "rarity", "quest_name")
    list_filter = ("rarity", "is_consumed")
