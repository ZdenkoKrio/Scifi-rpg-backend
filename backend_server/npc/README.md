# NPC Package

This package manages all non-player characters (NPCs) in the game, including merchants, quest givers, pirates, enemies, and faction members.

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

### `Merchant`
- Represents a specialized NPC that sells items.
- Has an associated inventory of items.
- Uses a `ManyToManyField` with the `Item` model via `MerchantInventory`.

### `MerchantInventory`
- Tracks which items a merchant has in stock.
- Includes item quantity and price.
- Connects merchants to items.

### `QuestGiver`
- Represents an NPC that provides quests.
- Has a `ManyToManyField` linking to `QuestItem`.
- Allows players to start, track, and complete missions.

## API Endpoints

### Base URL: `/npc/api/`

#### **NPCs**
| Method  | Endpoint            | Description                        |
|---------|---------------------|------------------------------------|
| `GET`   | `/npcs/`            | Retrieve all NPCs                 |
| `POST`  | `/npcs/`            | Create a new NPC                  |
| `GET`   | `/npcs/<id>/`       | Retrieve a single NPC             |
| `PUT`   | `/npcs/<id>/`       | Update an existing NPC            |
| `PATCH` | `/npcs/<id>/`       | Partially update an NPC           |
| `DELETE`| `/npcs/<id>/`       | Delete an NPC                     |

#### **Merchants**
| Method  | Endpoint            | Description                        |
|---------|---------------------|------------------------------------|
| `GET`   | `/merchants/`       | Retrieve all merchants            |
| `POST`  | `/merchants/`       | Create a new merchant             |
| `GET`   | `/merchants/<id>/`  | Retrieve a single merchant        |
| `PUT`   | `/merchants/<id>/`  | Update an existing merchant       |
| `PATCH` | `/merchants/<id>/`  | Partially update a merchant       |
| `DELETE`| `/merchants/<id>/`  | Delete a merchant                 |

#### **Merchant Inventory**
| Method  | Endpoint                 | Description                        |
|---------|--------------------------|------------------------------------|
| `GET`   | `/merchant-inventory/`   | Retrieve merchant inventory       |
| `POST`  | `/merchant-inventory/`   | Add an item to a merchant's stock |
| `GET`   | `/merchant-inventory/<id>/` | Retrieve a specific stock entry  |
| `PUT`   | `/merchant-inventory/<id>/` | Update stock quantity or price  |
| `PATCH` | `/merchant-inventory/<id>/` | Partially update stock entry    |
| `DELETE`| `/merchant-inventory/<id>/` | Remove an item from stock        |

#### **Quest Givers**
| Method  | Endpoint            | Description                        |
|---------|---------------------|------------------------------------|
| `GET`   | `/quest-givers/`    | Retrieve all quest givers         |
| `POST`  | `/quest-givers/`    | Create a new quest giver          |
| `GET`   | `/quest-givers/<id>/` | Retrieve a single quest giver    |
| `PUT`   | `/quest-givers/<id>/` | Update an existing quest giver   |
| `PATCH` | `/quest-givers/<id>/` | Partially update a quest giver   |
| `DELETE`| `/quest-givers/<id>/` | Delete a quest giver             |

## Commands

### `seed_npc.py`
- Seeds the database with test NPC characters.
- Run using:
  ```bash
  python manage.py seed_npc