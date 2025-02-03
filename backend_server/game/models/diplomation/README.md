# Diplomation Package

This package handles the relationships between species and factions in the game.

## Models

### `Faction`
- Represents a galactic political entity with:
  - **Allies and enemies**
  - **Controlled star systems**
  - **Capital star system**

### `Species`
- Represents a sentient or non-sentient race in the galaxy.
- Can be:
  - **Intelligent** – Technologically advanced civilizations.
  - **Primitive** – Developing or tribal civilizations.
  - **Animal** – Wildlife and non-sentient creatures.
  - **Synthetic AI** – Fully artificial lifeforms.

### `SpeciesFaction`
- Represents how species are integrated into factions.
- A species can be:
  - **Majority Population** – The dominant race in the faction.
  - **Minority Population** – A smaller group within the faction.
  - **Rulers** – The ruling elite.
  - **Slaves** – Enslaved members of the faction.

## Commands

### `seed_diplomation.py`
- Seeds the database with sample faction-species relationships.
- Run using:
  ```bash
  python manage.py seed_diplomation