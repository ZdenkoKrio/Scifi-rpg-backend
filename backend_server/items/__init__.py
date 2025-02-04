"""
Items Module

This package manages all in-game items, including weapons, armor, jewelry, and quest items.

## Included Models:
- `Item` → Base model for all in-game items.
- `Weapon` → Inherits from `Item`, includes attack-related stats.
- `Armor` → Inherits from `Item`, provides defensive bonuses.
- `Jewelry` → Inherits from `Item`, serves as collectible or valuable artifacts.
- `QuestItem` → Inherits from `Item`, used for mission objectives.

## Usage:
- Weapons define base damage, critical hit chance, and bonus effects.
- Armor provides defensive stats and special resistances.
- Jewelry serves as rare collectibles with lore-based origins.
- Quest items are used for mission progress and may be consumable.

"""

from .models import Item, ITEM_RARITIES, Weapon, Armor, Jewelry, QuestItem
