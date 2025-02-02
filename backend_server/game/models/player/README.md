# Game Models

This directory contains all models related to the game mechanics.

## Models

### `Player`
- Represents a player's in-game character.
- Tracks level, stats, economy, and combat records.
- Equipped items reference `Weapon` and `Armor`.

### `Reputation`
- Tracks a player's standing with different factions.
- Can have positive or negative values.

### `Resistance`
- Defines a player's resistance to plasma, EMP, or radiation damage.

### `Skill`
- Represents abilities a player can use in combat.
- Includes cooldowns and special effects.

### `PlayerItem`
- Tracks inventory, linking a `Player` to their `Item`s.
- Allows for equipping weapons and armor.
