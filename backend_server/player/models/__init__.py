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

import importlib

Player = importlib.import_module(".Player", package="player.models").Player
PlayerItem = importlib.import_module(".PlayerItem", package="player.models").PlayerItem
Reputation = importlib.import_module(".Reputation", package="player.models").Reputation
Resistance = importlib.import_module(".Resistance", package="player.models").Resistance
Skill = importlib.import_module(".Skill", package="player.models").Skill

__all__ = ["Player", "PlayerItem", "Reputation", "Resistance", "Skill"]
