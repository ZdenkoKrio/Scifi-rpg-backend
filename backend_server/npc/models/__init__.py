"""
NPC Module

This package contains models related to Non-Player Characters (NPCs) in the game.

## Included Models:
- `NPC` → Base model for all non-player characters.
- `Merchant` → Special type of NPC that sells items.
- `MerchantInventory` → Tracks which items a merchant sells and their prices.
- `QuestGiver` → Special type of NPC that provides quests to players.

## Usage:
- NPCs can belong to factions and have various roles (e.g., merchants, bounty hunters, pirates).
- Merchants maintain a dynamic inventory of items with adjustable stock and prices.
- Quest givers distribute quests and track available missions.

"""

from .NPC import NPC
from .Merchant import Merchant, MerchantInventory
from .QuestGiver import QuestGiver
