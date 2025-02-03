from django.contrib import admin
from .models import NPC, Merchant, MerchantInventory, QuestGiver


@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    """Admin panel for NPCs."""
    list_display = ("name", "role", "level", "faction", "reputation_effect")
    search_fields = ("name", "role")
    list_filter = ("role", "faction")

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    """Admin panel for Merchants."""
    list_display = ("npc",)
    search_fields = ("npc__name",)

@admin.register(MerchantInventory)
class MerchantInventoryAdmin(admin.ModelAdmin):
    """Admin panel for Merchant Inventory."""
    list_display = ("merchant", "item", "quantity", "price")
    search_fields = ("merchant__npc__name", "item__name")

@admin.register(QuestGiver)
class QuestGiverAdmin(admin.ModelAdmin):
    """Admin panel for Quest Givers."""
    list_display = ("npc",)
    search_fields = ("npc__name",)