from django.contrib import admin
from .models import Player, PlayerItem, Reputation, Resistance, Skill


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Admin panel for players."""
    list_display = ("user", "level", "class_type", "credits", "experience")
    search_fields = ("user__username",)
    list_filter = ("class_type", "level")


@admin.register(PlayerItem)
class PlayerItemAdmin(admin.ModelAdmin):
    """Admin panel for player inventory."""
    list_display = ("player", "item", "quantity", "is_equipped")
    search_fields = ("player__user__username", "item__name")


@admin.register(Reputation)
class ReputationAdmin(admin.ModelAdmin):
    """Admin panel for player reputation."""
    list_display = ("player", "faction", "value")
    search_fields = ("player__user__username", "faction__name")


@admin.register(Resistance)
class ResistanceAdmin(admin.ModelAdmin):
    """Admin panel for player resistances."""
    list_display = ("player", "type", "value")
    search_fields = ("player__user__username",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin panel for player skills."""
    list_display = ("name", "effect", "cooldown")
    search_fields = ("name",)
