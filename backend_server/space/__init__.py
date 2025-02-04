"""
🌌 Space Package

This package manages all celestial bodies, star systems, and spatial phenomena in the game world.

## Modules

- `models` - Defines all celestial objects such as stars, planets, moons, space stations, asteroids, nebulas, and unknown objects.
- `api` - Provides a RESTful API for querying celestial data.
- `management.commands` - Includes database seed commands for generating star systems, planets, and other objects.
- `admin` - Configures the Django admin panel for managing space-related objects.

## Dependencies
- `diplomation` - Faction control over star systems.
- `game` - Core game logic and interactions.

## Main Features
- **Star Systems** - Fully explorable systems with procedurally generated celestial objects.
- **Planets & Moons** - Habitable and non-habitable planetary bodies with economic and atmospheric data.
- **Asteroids & Nebulas** - Rich in resources but may pose dangers such as pirate activity or storms.
- **Space Stations** - Trade, military, and research hubs orbiting various celestial bodies.
- **Unknown Objects** - Mysterious anomalies, artifacts, and derelict stations waiting to be discovered.

🚀 *Use the `seed_space` command to populate the galaxy with objects.*

"""
from .models import CelestialBody, StarSystem, Star, Planet, Moon, SpaceStation, Asteroid, Nebula, UnknownObject
