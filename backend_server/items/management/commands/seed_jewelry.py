from django.core.management.base import BaseCommand
from items import Jewelry


class Command(BaseCommand):
    """Seeds the database with a set of rare jewelry items."""
    help = "Seed the database with rare jewelry."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding jewelry...")

        jewelry_items = [
            {"name": "Galactic Crown", "rarity": "legendary", "origin": "Lost Empire of Velaria"},
            {"name": "Quantum Pendant", "rarity": "rare", "origin": "AI Collective Relic"},
            {"name": "Star Ruby", "rarity": "epic", "origin": "Asteroid Belt X-29"},
            {"name": "Black Hole Gem", "rarity": "legendary", "origin": "Unknown Singularity"},
            {"name": "Solar Emerald", "rarity": "epic", "origin": "Dying Star Nebula"},
            {"name": "Frozen Diamond", "rarity": "rare", "origin": "Ice Planet Eryon"},
            {"name": "Celestial Sapphire", "rarity": "uncommon", "origin": "Moon Base Zeta"},
            {"name": "Nebula Pearl", "rarity": "legendary", "origin": "Triton Nebula"},
            {"name": "Time Crystal", "rarity": "epic", "origin": "Chrono Rift"},
            {"name": "Dark Matter Amulet", "rarity": "rare", "origin": "Quantum Lab Alpha"},
            {"name": "Void Pendant", "rarity": "common", "origin": "Abandoned Research Station"},
            {"name": "Eclipse Ring", "rarity": "epic", "origin": "Black Dwarf Colony"},
            {"name": "Solaris Amulet", "rarity": "rare", "origin": "System Helios Prime"},
            {"name": "Cosmic Bracelet", "rarity": "uncommon", "origin": "Exiled Ship Graveyard"},
            {"name": "Wormhole Key", "rarity": "legendary", "origin": "Temporal Distortion Field"},
            {"name": "Hyperion Jewel", "rarity": "epic", "origin": "Forgotten Vault of Hyperion"},
            {"name": "Frozen Moonstone", "rarity": "rare", "origin": "Moon Kaldar"},
            {"name": "Crimson Opal", "rarity": "uncommon", "origin": "Bounty Hunter's Market"},
            {"name": "Psionic Amulet", "rarity": "epic", "origin": "Psionic Academy"},
            {"name": "Warp Crystal", "rarity": "legendary", "origin": "Subspace Rift"},
        ]

        for jewelry_data in jewelry_items:
            Jewelry.objects.get_or_create(**jewelry_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded jewelry!"))
