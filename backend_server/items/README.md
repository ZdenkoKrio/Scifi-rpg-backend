# Inventory System

This module manages the player's inventory, including weapons, armor, jewelry, quest items, and consumables.

## Models

### `Item`
- Abstract base model for all items in the game.
- Contains common attributes such as `name`, `description`, `value`, and `rarity`.
- Uses predefined **rarity levels**: `common`, `uncommon`, `rare`, `epic`, `legendary`.

### `Weapon`
- Inherits from `Item`.
- Includes attributes for base damage, critical chance, and critical hit bonus.

### `Armor`
- Inherits from `Item`.
- Includes attributes for defense and special effects.

### `Jewelry`
- Inherits from `Item`.
- Represents collectible or valuable items with no direct gameplay effects.
- Includes an `origin` attribute indicating where the item was found.

### `QuestItem`
- Inherits from `Item`.
- Used for mission-related objectives.
- Includes attributes for `quest_name` and `is_consumed` (determines if the item disappears after use).

### `PlayerInventory`
- A one-to-one relationship with `User`.
- Stores references to items owned by the player.

### `PlayerItem`
- A through model linking `PlayerInventory` to `Item` with a quantity.
- Supports **equipped status** (`is_equipped` flag) to indicate currently used gear.

## Constants

### `ITEM_RARITIES`
- A predefined list of item rarities used in all item models.
- Ensures consistency and prevents incorrect values.

### `RARITY_DESCRIPTIONS`
- Dictionary mapping item rarities to detailed descriptions.
- Used to retrieve rarity descriptions dynamically.

## Commands

### `seed_items.py`
- Seeds the database with a predefined set of weapons, armor, jewelry, quest items, and consumables.
- Run using:
  ```bash
  python manage.py seed_items