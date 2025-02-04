from django.db import models


SPECIES_FACTION_ROLES = [
    ("majority", "Majority Population"),
    ("minority", "Minority Population"),
    ("rulers", "Ruling Class"),
    ("slaves", "Enslaved Population"),
]


class SpeciesFaction(models.Model):
    """Represents the relationship between species and factions."""
    species = models.ForeignKey("Species", on_delete=models.CASCADE, related_name="faction_affiliations")
    faction = models.ForeignKey("Faction", on_delete=models.CASCADE, related_name="species_members")
    role_in_faction = models.CharField(max_length=30, choices=SPECIES_FACTION_ROLES)

    def __str__(self):
        return f"{self.species.name} in {self.faction.name} as {self.role_in_faction}"
