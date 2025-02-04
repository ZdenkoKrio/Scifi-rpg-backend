from django.contrib import admin
from .models import StarSystem, Star, Planet, Moon, SpaceStation, Asteroid, Nebula, UnknownObject


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = ("name", "faction", "coordinates_x", "coordinates_y", "coordinates_z")
    search_fields = ("name",)


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ("name", "star_type", "temperature", "size", "luminosity", "star_system")
    list_filter = ("star_type",)


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("name", "star_system", "atmosphere_type", "population", "economy_type")
    list_filter = ("economy_type",)


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    list_display = ("name", "planet", "composition", "resource_richness")


@admin.register(SpaceStation)
class SpaceStationAdmin(admin.ModelAdmin):
    list_display = ("name", "station_type", "owner_faction", "orbiting_object", "star_system")


@admin.register(Asteroid)
class AsteroidAdmin(admin.ModelAdmin):
    list_display = ("name", "star_system", "is_mining_site", "has_pirate_activity")


@admin.register(Nebula)
class NebulaAdmin(admin.ModelAdmin):
    list_display = ("name", "gas_composition", "visibility", "has_storms")


@admin.register(UnknownObject)
class UnknownObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "object_type", "danger_level", "scientific_value", "star_system")
    