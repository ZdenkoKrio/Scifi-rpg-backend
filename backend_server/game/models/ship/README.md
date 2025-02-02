# Ship Package

This package manages all spaceship-related mechanics, including player-owned ships, weapons, armor, upgrades, and crew.

## Models

### `Ship`
- Represents a spaceship owned by a player.
- Includes attributes such as:
  - `hp`, `shield`, `speed`, `cargo_capacity`
  - `weapon_slots`, `armor_slots`, `crew_capacity`
- Can be upgraded with weapons, armor, and ship modifications.

### `ShipWeapon`
- Represents weapons mounted on a ship.
- Defines properties like damage, energy consumption, and critical hit chance.

### `ShipArmor`
- Represents armor installed on a ship.
- Provides defensive bonuses and special effects.

### `ShipUpgrade`
- Represents modules that enhance a ship's abilities.
- Some upgrades provide passive bonuses, while others consume energy.

### `ShipCrew`
- Represents crew members assigned to a spaceship.
- Each crew member has a specific role (`pilot`, `engineer`, `gunner`, `medic`, `scientist`).
- Crew members can be unique or recruited from the `NPC` pool.

## Commands

### `seed_ships.py`
- Seeds the database with test player ships.
- Run using:
  ```bash
  python manage.py seed_ships