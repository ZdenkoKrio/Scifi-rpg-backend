from django.db import models
from .Species import Species


class SpeciesFaction(models.Model):
    """Represents the relationship between species and factions."""
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="faction_affiliations")
    faction = models.ForeignKey("Faction", on_delete=models.CASCADE, related_name="species_members")
    role_in_faction = models.CharField(max_length=100, choices=[
        ("majority", "Majority Population"),
        ("minority", "Minority Population"),
        ("rulers", "Ruling Class"),
        ("slaves", "Enslaved Population"),
    ])

    def __str__(self):
        return f"{self.species.name} in {self.faction.name} as {self.role_in_faction}"
