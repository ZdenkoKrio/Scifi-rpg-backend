# 🌌 Space Package

This package manages all celestial bodies, star systems, and space phenomena in the game world.

## 📖 Overview

The `space` package defines and handles all space-related objects, such as **star systems, planets, moons, space stations, asteroids, nebulas, and unknown objects**. 
It supports procedural galaxy generation and API endpoints for querying celestial data.

## 🛠 Features

- **Procedural Star Systems** – Each star system has a unique name, coordinates, and a central star.
- **Planets & Moons** – Planets have atmospheric properties, populations, and economic types.
- **Asteroids & Mining** – Some asteroids serve as mining sites or hide pirate activity.
- **Nebulas & Space Phenomena** – Nebulas vary in gas composition, visibility, and hazards.
- **Space Stations** – Trading hubs, military bases, and research stations, orbiting celestial objects or freely floating.
- **Unknown Objects** – Mysterious artifacts, wormholes, and derelict stations waiting to be discovered.
- **Faction Ownership** – Star systems can be controlled by different factions.

## 📂 Models

### `StarSystem`
- Represents a star system with unique coordinates in space.
- Can be controlled by a **Faction** or remain neutral.

### `Star`
- A single star at the center of each **StarSystem**.
- Has different types: `Main Sequence`, `Red Giant`, `White Dwarf`, `Neutron Star`, `Black Hole`.

### `Planet`
- Represents a planet within a **StarSystem**.
- Has an **atmosphere type**, **population**, and **economy type**.

### `Moon`
- Represents a **moon** orbiting a planet.
- Can have **mining colonies** or **military bases**.

### `SpaceStation`
- Represents space stations in orbit around planets or floating freely.
- Can be **Trading Stations**, **Military Bases**, or **Research Facilities**.

### `Asteroid`
- Represents an asteroid in space.
- May be a **mining site** or have **pirate activity**.

### `Nebula`
- Represents a nebula in space.
- Can be rich in **resources** or dangerous due to **storms**.

### `UnknownObject`
- Represents unknown anomalies such as **black holes, wormholes, and alien artifacts**.
- Has **scientific value** and a **danger level**.

## 🚀 API Endpoints

| **Endpoint** | **Description** | **Methods** |
|-------------|---------------|------------|
| `/api/space/star-systems/` | List and manage star systems | GET, POST, PUT, DELETE |
| `/api/space/stars/` | List and manage stars | GET, POST, PUT, DELETE |
| `/api/space/planets/` | List and manage planets | GET, POST, PUT, DELETE |
| `/api/space/moons/` | List and manage moons | GET, POST, PUT, DELETE |
| `/api/space/space-stations/` | List and manage space stations | GET, POST, PUT, DELETE |
| `/api/space/asteroids/` | List and manage asteroids | GET, POST, PUT, DELETE |
| `/api/space/nebulas/` | List and manage nebulas | GET, POST, PUT, DELETE |
| `/api/space/unknown-objects/` | List and manage unknown objects | GET, POST, PUT, DELETE |

## ⚙️ Commands

### `seed_space.py`
Populates the database with procedurally generated space objects.

#### Individual Commands:
```bash
python manage.py seed_star_systems        # Generates 20 star systems
python manage.py seed_stars               # Adds stars to star systems
python manage.py seed_planets             # Populates systems with planets
python manage.py seed_moons               # Adds moons to planets
python manage.py seed_asteroids           # Generates asteroid belts
python manage.py seed_nebulas             # Creates gas clouds in space
python manage.py seed_space_stations      # Populates stations in orbit
python manage.py seed_unknown_objects     # Adds anomalies and black holes