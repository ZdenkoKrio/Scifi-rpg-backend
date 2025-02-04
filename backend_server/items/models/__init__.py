"""
Package for item models in the game.

This package contains:
- `ITEM_RARITIES` (list of available rarities)
- `RARITY_DESCRIPTIONS` (dictionary of rarity descriptions) -- non-actual
- `Item` (abstract base class)
- `Weapon`
- `Armor`
- `Jewelry` (rare collectibles)
- `QuestItem` (mission-related items)
"""
from django.apps import apps
from .Item import ITEM_RARITIES

def get_item_models():
    return (
        apps.get_model("items", "Item"),
        apps.get_model("items", "Weapon"),
        apps.get_model("items", "Armor"),
        apps.get_model("items", "Jewelry"),
        apps.get_model("items", "QuestItem"),
    )

__all__ = ["get_item_models", "ITEM_RARITIES"]
