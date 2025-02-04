"""
Space Models Package

This package contains all models related to space, including celestial bodies, planets, moons, asteroid fields, and deep-space anomalies.

## Included Models:
- `CelestialBody` → Abstract model for all space objects.
- `StarSystem` → Represents a solar system with a central star.
- `Star` → Different types of stars, including black holes.
- `Planet` → Planets with populations, atmosphere, and economic attributes.
- `Moon` → Moons that orbit planets, some with military or mining operations.
- `Asteroid` → Asteroids that can be mined or contain pirate activity.
- `Nebula` → Large space clouds with potential resources and hazards.
- `SpaceStation` → Artificial structures used for trade, research, or military purposes.
- `UnknownObject` → Unexplored or mysterious space anomalies.

## API:
- Provides RESTful access to all space objects.
- Allows querying for planetary systems, celestial objects, and stations.

## Commands:
- `seed_star_systems.py` → Populates the database with test star systems.
- `seed_celestial_bodies.py` → Generates planets, moons, asteroids, and nebulae.
- `seed_unknown_objects.py` → Creates anomalies and space mysteries.

## Future Enhancements:
- Implement dynamic space exploration.
- Generate procedural star systems.
- Add deep-space phenomena that change over time.
"""

from .celestial_body import CelestialBody
from .star_system import StarSystem
from .star import Star
from .planet import Planet
from .moon import Moon
from .asteroid import Asteroid
from .nebula import Nebula
from .space_station import SpaceStation
from .unknown_object import UnknownObject