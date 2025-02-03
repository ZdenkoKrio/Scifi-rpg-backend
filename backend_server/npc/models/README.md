# NPC Package

This package manages all non-player characters (NPCs) in the game, including merchants, pirates, enemies, and faction members.

## Models

### `NPC`
- Represents a general non-player character (NPC) in the game.
- Can belong to different roles such as:
  - `merchant` (sells items)
  - `bounty_hunter` (engages in combat)
  - `pirate` (steals cargo)
  - `officer` (works for factions)
  - `scientist` (provides research benefits)
  - `enemy` (hostile NPC)
  - `ally` (friendly NPC)
- Can be affiliated with a faction.
- Stores possible dialogue interactions.
- Can influence a player's reputation.

## Commands

### `seed_npc.py`
- Seeds the database with test NPC characters.
- Run using:
  ```bash
  python manage.py seed_npc