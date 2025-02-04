"""
Player Module

This package manages all player-related mechanics, including attributes, inventory, reputation, resistances, and skills.

## Included Models:
- `Player` → Stores the core attributes and statistics of a player.
- `PlayerItem` → Tracks player inventory, including equipped items.
- `Reputation` → Manages faction relationships and standing.
- `Resistance` → Defines a player's resistance to different damage types.
- `Skill` → Represents skills that players can use in combat.

## API Endpoints:
- **Players:** `/player/api/players/`
- **Inventory:** `/player/api/inventory/`
- **Reputation:** `/player/api/reputation/`
- **Resistance:** `/player/api/resistance/`
- **Skills:** `/player/api/skills/`

## Usage:
- Players have RPG-like attributes including level, experience, and equipment.
- Reputation affects how NPCs and factions interact with the player.
- Resistances influence how much damage the player takes from different attacks.
- Inventory management allows equipping, using, and trading items.

## Admin Panel Configuration:
- **Players** → Searchable by username, filterable by class type and level.
- **Inventory** → Displays items owned by a player.
- **Reputation** → Shows faction affiliations and reputation values.
- **Resistances** → Displays player's resistances to different damage types.
- **Skills** → Shows available skills with cooldown effects.

## Future Enhancements:
- Implement an advanced inventory system with storage limits.
- Add skill progression and unlockable perks.
- Introduce a marketplace where players can trade items.
"""

