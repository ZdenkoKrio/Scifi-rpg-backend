from django.contrib import admin
from django.apps import apps


class ItemsAdminConfig(admin.AdminSite):
    "Custom AdminSite to register items models safely."
    def ready(self):
        Weapon = apps.get_model("items", "Weapon")
        Armor = apps.get_model("items", "Armor")
        Jewelry = apps.get_model("items", "Jewelry")
        QuestItem = apps.get_model("items", "QuestItem")

        @admin.register(Weapon)
        class WeaponAdmin(admin.ModelAdmin):
            list_display = ("name", "rarity", "base_damage", "critical_chance", "critical_damage_bonus")
            search_fields = ("name", "rarity")
            list_filter = ("rarity",)

        @admin.register(Armor)
        class ArmorAdmin(admin.ModelAdmin):
            list_display = ("name", "rarity", "defense_bonus", "special_effect")
            search_fields = ("name", "rarity")
            list_filter = ("rarity",)

        @admin.register(Jewelry)
        class JewelryAdmin(admin.ModelAdmin):
            list_display = ("name", "rarity", "origin")
            search_fields = ("name", "rarity", "origin")
            list_filter = ("rarity",)

        @admin.register(QuestItem)
        class QuestItemAdmin(admin.ModelAdmin):
            list_display = ("name", "rarity", "quest_name", "is_consumed")
            search_fields = ("name", "rarity", "quest_name")
            list_filter = ("rarity", "is_consumed")

admin.site = ItemsAdminConfig()
