# Diplomation Package

This package manages the relationships between factions and species in the game, including alliances, territorial control, and societal structures.

## Models

### `Faction`
- Represents a galactic political entity with:
  - **Allies and enemies** – Factions can form alliances or engage in wars.
  - **Controlled star systems** – Determines territorial expansion.
  - **Capital star system** – The main headquarters of the faction.

### `Species`
- Represents a sentient or non-sentient race in the galaxy.
- Can be:
  - **Intelligent** – Technologically advanced civilizations.
  - **Primitive** – Developing or tribal civilizations.
  - **Animal** – Wildlife and non-sentient creatures.
  - **Synthetic AI** – Fully artificial lifeforms.
- Has unique biological characteristics such as:
  - **Homeworld** – The planet of origin.
  - **Lifespan** – The average life expectancy.
  - **Average height** – The species' typical size.

### `SpeciesFaction`
- Represents how species are integrated into factions.
- A species can be:
  - **Majority Population** – The dominant race in the faction.
  - **Minority Population** – A smaller group within the faction.
  - **Rulers** – The ruling elite.
  - **Slaves** – Enslaved members of the faction.

## API Endpoints

### Base URL: `/diplomation/api/`

#### **Factions**
| Method  | Endpoint               | Description                        |
|---------|------------------------|------------------------------------|
| `GET`   | `/factions/`           | Retrieve all factions              |
| `POST`  | `/factions/`           | Create a new faction               |
| `GET`   | `/factions/<id>/`      | Retrieve a specific faction        |
| `PUT`   | `/factions/<id>/`      | Update an existing faction         |
| `DELETE`| `/factions/<id>/`      | Delete a faction                   |

#### **Species**
| Method  | Endpoint               | Description                        |
|---------|------------------------|------------------------------------|
| `GET`   | `/species/`            | Retrieve all species               |
| `POST`  | `/species/`            | Create a new species               |
| `GET`   | `/species/<id>/`       | Retrieve a specific species        |
| `PUT`   | `/species/<id>/`       | Update an existing species         |
| `DELETE`| `/species/<id>/`       | Delete a species                   |

#### **Species-Faction Relations**
| Method  | Endpoint                  | Description                          |
|---------|---------------------------|--------------------------------------|
| `GET`   | `/species-factions/`       | Retrieve all species-faction links  |
| `POST`  | `/species-factions/`       | Create a new species-faction link   |
| `GET`   | `/species-factions/<id>/`  | Retrieve a specific species-faction link |
| `PUT`   | `/species-factions/<id>/`  | Update a species-faction link       |
| `DELETE`| `/species-factions/<id>/`  | Delete a species-faction link       |

## Commands

### `seed_factions.py`
- Seeds the database with predefined factions.
- Run using:
  ```bash
  python manage.py seed_factions