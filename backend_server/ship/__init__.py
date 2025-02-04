"""
Ship Management Package

This package contains all models and functionalities related to spaceships in the game.

## Included Models:
- `Ship` → Represents a player's spaceship with upgradeable attributes.
- `ShipArmor` → Armor modules installed on ships to increase defense.
- `ShipWeapon` → Weapons mounted on spaceships, affecting damage and energy consumption.
- `ShipUpgrade` → Enhancements that modify ship capabilities.
- `ShipCrew` → Crew members assigned to ships, each with a specific role.

## API:
- Ships and their components can be accessed and modified via REST API endpoints.
- Fully integrated with Django Admin for management.

## Commands:
- `seed_ships.py` → Populates the database with ships and owners.
- `seed_ship_equipment.py` → Generates weapons, armor, and upgrades.
- `seed_ship_crew.py` → Assigns crew members to ships.
- `seed_all_ships.py` → Runs all seed commands in the correct order.

## Future Enhancements:
- Implement ship trading and economic systems.
- Introduce battle mechanics with ship-to-ship combat.
"""

