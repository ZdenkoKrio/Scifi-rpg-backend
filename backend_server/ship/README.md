# Ship Package

This package manages all spaceship-related mechanics, including player-owned ships, weapons, armor, upgrades, and crew.

## Models

### `Ship`
- Represents a spaceship owned by a player.
- Includes attributes such as:
  - **Health stats:** `hp`, `max_hp`, `shield`, `max_shield`
  - **Capabilities:** `speed`, `cargo_capacity`, `fuel_capacity`
  - **Customization slots:** `weapon_slots`, `armor_slots`, `crew_capacity`
- Ships can be **equipped with weapons, armor, and upgrades**.

### `ShipWeapon`
- Represents **weapons mounted on a spaceship**.
- Defines properties such as:
  - **Damage output**
  - **Critical hit chance**
  - **Energy consumption per shot**

### `ShipArmor`
- Represents **defensive armor installed on a spaceship**.
- Provides **damage resistance** and **special effects**, such as:
  - **Plasma resistance**
  - **EMP shielding**
  - **Kinetic absorption**

### `ShipUpgrade`
- Represents **modules that enhance a ship's abilities**.
- Upgrades can:
  - **Improve ship stats (e.g., speed boost, shield regen)**
  - **Provide passive bonuses or active energy-consuming effects**

### `ShipCrew`
- Represents **crew members assigned to a spaceship**.
- Each crew member has a **role**:
  - **Pilot** → Improves ship maneuverability.
  - **Engineer** → Boosts repair and maintenance efficiency.
  - **Gunner** → Increases weapon accuracy and fire rate.
  - **Medic** → Supports crew survival in emergencies.
  - **Scientist** → Enhances research-based ship upgrades.
- Crew members can be **unique NPCs or general recruits**.

## API Endpoints

| **Model**      | **Endpoint**                | **Description**                 |
|---------------|----------------------------|---------------------------------|
| Ships        | `/ship/api/ships/`          | List, create, retrieve, update, delete spaceships |
| Ship Weapons | `/ship/api/ship-weapons/`   | Manage spaceship weapons       |
| Ship Armor   | `/ship/api/ship-armor/`     | Manage spaceship armor         |
| Ship Upgrades | `/ship/api/ship-upgrades/` | Manage spaceship enhancements  |
| Ship Crew    | `/ship/api/ship-crew/`      | Manage ship personnel          |

## Commands

### `seed_ships.py`
- Seeds the database with **player ships**.
- Run using:
  ```bash
  python manage.py seed_ships

### `seed_ship_equipment.py`
- Populates the database with **ship weapons, armor, and upgrades**.
- Run using:
  ```bash
  python manage.py seed_ship_equipment

### `seed_ship_crew.py`
- Assigns **crew members to ships**.
- Run using:
  ```bash
  python manage.py seed_ship_crew

### `seed_all_ships.py`
- Runs all ship-related seed commands.
- Run using:
  ```bash
  python manage.py seed_all_ships

## Admin Panel Configuration

- **Ships** → Displays name, type, owner, HP, shields, speed.
- **Weapons** → Displays name, damage, energy consumption, assigned ship.
- **Armor** → Shows defense bonus, effects, ship assignments.
- **Upgrades** → Shows installed modules and their effects.
- **Crew** → Displays crew role, assigned ship, and skill level.

## Future Enhancements

- **Dynamic space combat mechanics** (ship-to-ship battles).
- **Fuel economy and ship maintenance systems**.
- **Ship trading and faction-based ownership**.
- **More complex crew interactions and AI behavior**.
