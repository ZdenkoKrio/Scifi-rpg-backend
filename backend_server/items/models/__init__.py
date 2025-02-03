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

from .Item import Item, ITEM_RARITIES  #, RARITY_DESCRIPTIONS
from .Weapon import Weapon
from .Armor import Armor
from .Jewelry import Jewelry
from .QuestItem import QuestItem
