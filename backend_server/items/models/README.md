# Inventory System

This module manages the player's inventory, including weapons, armor, and general items.

## Models

### `Item`
- Represents any in-game item.
- Supports multiple types: `weapon`, `armor`, `consumable`, `misc`.

### `Weapon`
- Inherits from `Item`.
- Includes attributes for base damage and critical hit properties.

### `Armor`
- Inherits from `Item`.
- Includes attributes for defense and special effects.

### `PlayerInventory`
- A one-to-one relationship with `User`.
- Stores references to items owned by the player.

### `PlayerInventoryItem`
- A through model linking `PlayerInventory` to `Item` with a quantity.

## Commands

### `seed_items.py`
- Seeds the database with a predefined set of weapons, armor, and general items.
- Run using:
  ```bash
  python manage.py seed_items