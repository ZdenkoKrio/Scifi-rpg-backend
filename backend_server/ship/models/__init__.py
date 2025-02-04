"""
Ship Models Package

This package contains all models related to spaceships, including ship attributes, weapons, armor, crew, and upgrades.

## Included Models:
- `Ship` → Represents a player's spaceship with upgradeable stats.
- `ShipArmor` → Armor modules installed on ships to increase defense.
- `ShipWeapon` → Weapons mounted on spaceships, affecting damage and energy consumption.
- `ShipUpgrade` → Enhancements that modify ship capabilities.
- `ShipCrew` → Crew members assigned to ships, each with a specific role.

## Usage:
- Players can own multiple ships, each with customizable attributes.
- Ships can be equipped with weapons, armor, and upgrades.
- Crew members improve ship performance based on their roles.

## Future Enhancements:
- Introduce ship **special abilities** (e.g., cloaking, overdrive).
- Expand **ship economy**, including fuel costs and repairs.
"""

from .Ship import Ship
from .ShipArmor import ShipArmor
from .ShipWeapon import ShipWeapon
from .ShipUpgrade import ShipUpgrade
from .ShipCrew import ShipCrew
