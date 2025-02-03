# Player Module

This directory contains all models related to player mechanics, including attributes, inventory, reputation, resistances, and skills.

## Models

### `Player`
- Represents a player's in-game character.
- Tracks core attributes such as level, experience, and economy.
- Includes RPG-like stats (strength, defense, agility, intelligence, luck).
- Keeps records of combat performance (fights won/lost, missions completed/failed).
- Equipped items reference `Weapon` and `Armor` from the `items` application.

### `PlayerItem`
- Tracks inventory, linking a `Player` to their `Item`s.
- Supports multiple quantities per item.
- Includes an `is_equipped` flag for tracking currently used gear.

### `Reputation`
- Tracks a player's standing with different factions.
- Can have positive or negative values.
- Uses a `ForeignKey` to `Faction` from the `diplomation` application.

### `Resistance`
- Defines a player's resistance to different damage types.
- Supports predefined resistance types: `plasma`, `EMP`, `radiation`.
- Used to calculate damage reduction.

### `Skill`
- Represents combat and utility abilities a player can use.
- Includes cooldowns and special effects.
- Can be expanded to include skill progression and upgrades.

## API Endpoints

### Base URL: `/player/api/`

#### **Players**
| Method  | Endpoint            | Description                        |
|---------|---------------------|------------------------------------|
| `GET`   | `/players/`         | Retrieve all players              |
| `POST`  | `/players/`         | Create a new player               |
| `GET`   | `/players/<id>/`    | Retrieve a specific player        |
| `PUT`   | `/players/<id>/`    | Update an existing player         |
| `PATCH` | `/players/<id>/`    | Partially update a player         |
| `DELETE`| `/players/<id>/`    | Delete a player                   |

#### **Inventory**
| Method  | Endpoint              | Description                           |
|---------|-----------------------|---------------------------------------|
| `GET`   | `/inventory/`         | Retrieve all inventory items          |
| `POST`  | `/inventory/`         | Add an item to a player's inventory   |
| `GET`   | `/inventory/<id>/`    | Retrieve a specific inventory item    |
| `PUT`   | `/inventory/<id>/`    | Update inventory item quantity/status |
| `PATCH` | `/inventory/<id>/`    | Partially update inventory item       |
| `DELETE`| `/inventory/<id>/`    | Remove an item from inventory         |

#### **Reputation**
| Method  | Endpoint             | Description                        |
|---------|----------------------|------------------------------------|
| `GET`   | `/reputation/`       | Retrieve all reputation records   |
| `POST`  | `/reputation/`       | Create a new reputation record    |
| `GET`   | `/reputation/<id>/`  | Retrieve a specific reputation    |
| `PUT`   | `/reputation/<id>/`  | Update a reputation record        |
| `PATCH` | `/reputation/<id>/`  | Partially update reputation       |
| `DELETE`| `/reputation/<id>/`  | Delete a reputation record        |

#### **Resistances**
| Method  | Endpoint             | Description                        |
|---------|----------------------|------------------------------------|
| `GET`   | `/resistance/`       | Retrieve all resistances          |
| `POST`  | `/resistance/`       | Create a new resistance record    |
| `GET`   | `/resistance/<id>/`  | Retrieve a specific resistance    |
| `PUT`   | `/resistance/<id>/`  | Update a resistance record        |
| `PATCH` | `/resistance/<id>/`  | Partially update resistance       |
| `DELETE`| `/resistance/<id>/`  | Delete a resistance record        |

#### **Skills**
| Method  | Endpoint         | Description                        |
|---------|----------------|------------------------------------|
| `GET`   | `/skills/`      | Retrieve all available skills     |
| `POST`  | `/skills/`      | Create a new skill                |
| `GET`   | `/skills/<id>/` | Retrieve a specific skill         |
| `PUT`   | `/skills/<id>/` | Update a skill                    |
| `PATCH` | `/skills/<id>/` | Partially update a skill          |
| `DELETE`| `/skills/<id>/` | Delete a skill                    |

## Admin Panel Configuration

All models are registered in Django Admin:
- **Players** → Searchable by username, filterable by class type and level.
- **Inventory** → Displays items owned by a player.
- **Reputation** → Shows faction affiliations and reputation values.
- **Resistances** → Displays player's resistances to different damage types.
- **Skills** → Shows available skills with cooldown effects.

To access the admin panel:
1. Create a superuser:
   ```bash
   python manage.py createsuperuser