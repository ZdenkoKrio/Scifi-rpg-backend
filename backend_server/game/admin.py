from django.contrib import admin
from .models import (
    Player, Weapon, Armor, Skill, PlayerSkill,
    ResistanceType, PlayerResistance,
    Faction, PlayerReputation,
    Item, PlayerInventory
)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("name", "base_damage", "critical_chance", "critical_damage_bonus")
    search_fields = ("name",)


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ("name", "defense_bonus", "special_effect")
    search_fields = ("name",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "level", "credits", "experience", "equipped_weapon", "equipped_armor")
    search_fields = ("username",)
    list_filter = ("level", "credits")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "base_cooldown")
    search_fields = ("name",)


@admin.register(PlayerSkill)
class PlayerSkillAdmin(admin.ModelAdmin):
    list_display = ("player", "skill", "level")
    search_fields = ("player__username", "skill__name")


@admin.register(ResistanceType)
class ResistanceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PlayerResistance)
class PlayerResistanceAdmin(admin.ModelAdmin):
    list_display = ("player", "resistance_type", "value")
    search_fields = ("player__username", "resistance_type__name")


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(PlayerReputation)
class PlayerReputationAdmin(admin.ModelAdmin):
    list_display = ("player", "faction", "value")
    search_fields = ("player__username", "faction__name")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "item_type", "value")
    search_fields = ("name",)


@admin.register(PlayerInventory)
class PlayerInventoryAdmin(admin.ModelAdmin):
    list_display = ("player", "item", "quantity")
    search_fields = ("player__username", "item__name")
