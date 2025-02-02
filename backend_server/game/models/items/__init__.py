"""
This package contains the core models for items and inventory in the game.

Modules:
- Item: Base model for all items in the game.
- Weapon: A subclass of Item representing weapons with critical hit properties.
- Armor: A subclass of Item representing armor with defensive properties.
"""

from .Item import Item
from .Weapon import Weapon
from .Armor import Armor
