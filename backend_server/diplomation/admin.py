from django.contrib import admin
from .models import Faction, Species, SpeciesFaction


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    """Admin panel for managing factions."""
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    """Admin panel for managing species."""
    list_display = ("name", "species_type", "homeworld", "lifespan", "average_height")
    search_fields = ("name", "species_type")


@admin.register(SpeciesFaction)
class SpeciesFactionAdmin(admin.ModelAdmin):
    """Admin panel for managing species-faction relationships."""
    list_display = ("species", "faction", "role_in_faction")
    search_fields = ("species__name", "faction__name")
