# Inventory System

This module manages the player's inventory, including weapons, armor, jewelry, quest items, and consumables.

## Models

### `Item`
- Base model for all items in the game.
- Contains common attributes such as `name`, `description`, `value`, and `rarity`.
- Uses predefined **rarity levels**: `common`, `uncommon`, `rare`, `epic`, `legendary`.
- Implements dynamic `get_rarity_display()` method for retrieving rarity labels.

### `Weapon`
- Inherits from `Item`.
- Includes attributes for `base_damage`, `critical_chance`, and `critical_damage_bonus`.

### `Armor`
- Inherits from `Item`.
- Includes attributes for `defense_bonus` and `special_effect`.

### `Jewelry`
- Inherits from `Item`.
- Represents collectible or valuable items with no direct gameplay effects.
- Includes an `origin` attribute indicating where the item was found.

### `QuestItem`
- Inherits from `Item`.
- Used for mission-related objectives.
- Includes attributes for `quest_name` and `is_consumed` (determines if the item disappears after use).

## API Endpoints

### Base URL: `/items/api/`

#### **Weapons**
| Method  | Endpoint                | Description                     |
|---------|-------------------------|---------------------------------|
| `GET`   | `/weapons/`              | Retrieve all weapons           |
| `POST`  | `/weapons/`              | Create a new weapon            |
| `GET`   | `/weapons/<id>/`         | Retrieve a single weapon       |
| `PUT`   | `/weapons/<id>/`         | Update an existing weapon      |
| `PATCH` | `/weapons/<id>/`         | Partially update a weapon      |
| `DELETE`| `/weapons/<id>/`         | Delete a weapon                |

#### **Armor**
| Method  | Endpoint                | Description                     |
|---------|-------------------------|---------------------------------|
| `GET`   | `/armors/`               | Retrieve all armor pieces      |
| `POST`  | `/armors/`               | Create a new armor             |
| `GET`   | `/armors/<id>/`          | Retrieve a single armor        |
| `PUT`   | `/armors/<id>/`          | Update an existing armor       |
| `PATCH` | `/armors/<id>/`          | Partially update an armor      |
| `DELETE`| `/armors/<id>/`          | Delete an armor                |

#### **Jewelry**
| Method  | Endpoint                | Description                     |
|---------|-------------------------|---------------------------------|
| `GET`   | `/jewelry/`              | Retrieve all jewelry items     |
| `POST`  | `/jewelry/`              | Create a new jewelry item      |
| `GET`   | `/jewelry/<id>/`         | Retrieve a single jewelry item |
| `PUT`   | `/jewelry/<id>/`         | Update an existing jewelry     |
| `PATCH` | `/jewelry/<id>/`         | Partially update a jewelry     |
| `DELETE`| `/jewelry/<id>/`         | Delete a jewelry item          |

#### **Quest Items**
| Method  | Endpoint                | Description                     |
|---------|-------------------------|---------------------------------|
| `GET`   | `/quest-items/`          | Retrieve all quest items       |
| `POST`  | `/quest-items/`          | Create a new quest item        |
| `GET`   | `/quest-items/<id>/`     | Retrieve a single quest item   |
| `PUT`   | `/quest-items/<id>/`     | Update an existing quest item  |
| `PATCH` | `/quest-items/<id>/`     | Partially update a quest item  |
| `DELETE`| `/quest-items/<id>/`     | Delete a quest item            |

## Constants

### `ITEM_RARITIES`
- A predefined list of item rarities used in all item models.
- Ensures consistency and prevents incorrect values.

### `RARITY_DESCRIPTIONS`
- Dictionary mapping item rarities to detailed descriptions.
- Used to retrieve rarity descriptions dynamically.

## Commands

### `seed_weapons.py`
- Seeds the database with a predefined set of **weapons**.
- Run using:
  ```bash
  python manage.py seed_weapons