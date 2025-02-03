"""
Player Module

This package manages all player-related mechanics, including attributes, inventory, reputation, resistances, and skills.

## Included Models:
- `Player` → Stores the core attributes and statistics of a player.
- `PlayerItem` → Tracks player inventory, including equipped items.
- `Reputation` → Manages faction relationships and standing.
- `Resistance` → Defines a player's resistance to different damage types.
- `Skill` → Represents skills that players can use in combat.

## Usage:
- Players have RPG-like attributes including level, experience, and equipment.
- Reputation affects how NPCs and factions interact with the player.
- Resistances influence how much damage the player takes from different attacks.
- Inventory management allows equipping, using, and trading items.

"""

from .Player import Player
from .PlayerItem import PlayerItem
from .Reputation import Reputation
from .Resistance import Resistance
from .Skill import Skill
