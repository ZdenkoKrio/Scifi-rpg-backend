"""
Diplomation Module

This package manages factions, species, and their diplomatic relationships.

## Included Models:
- `Faction` → Represents major galactic organizations, including their allies, enemies, and controlled systems.
- `Species` → Represents sentient and non-sentient species, including their homeworlds and biological traits.
- `SpeciesFaction` → Defines the relationship between species and factions, such as rulers, slaves, or minority populations.

## API Endpoints:
- **Factions:** `/diplomation/api/factions/`
- **Species:** `/diplomation/api/species/`
- **Species-Faction Relations:** `/diplomation/api/species-factions/`

## Admin Panel Configuration:
- **Factions** → Displays names, descriptions, and alliances.
- **Species** → Shows biological traits and homeworlds.
- **Species-Faction Relations** → Displays racial compositions of factions.

## Usage:
- Factions control star systems and form alliances or wars.
- Species belong to factions and shape their political and social structures.
- Diplomacy affects gameplay, influencing trade, wars, and player reputation.

## Future Enhancements:
- Implement dynamic diplomacy with trade agreements and war declarations.
- Introduce AI-controlled faction decision-making.
"""

from .models import Faction, Species, SpeciesFaction
