from django.core.management.base import BaseCommand
from npc import NPC, Merchant, MerchantInventory
from items import Item
from diplomation import Faction


class Command(BaseCommand):
    """Seeds the database with merchants and their inventory."""
    help = "Populate the database with test merchants and inventory."

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database with merchants...")

        merchants = [
            {"name": "Zalron the Trader", "faction": "Independent"},
            {"name": "Vexis Supplies", "faction": "Galactic Federation"},
            {"name": "Draknos Black Market", "faction": "Void Pirates"},
            {"name": "Cyber Emporium", "faction": "Independent"},
            {"name": "Federation Arsenal", "faction": "Galactic Federation"},
        ]

        for merchant in merchants:
            faction, _ = Faction.objects.get_or_create(name=merchant["faction"], defaults={"description": "Faction description"})
            npc = NPC.objects.create(
                name=merchant["name"],
                role="merchant",
                level=3,
                faction=faction,
                dialogue=f"Looking for the best deals in the galaxy?",
                reputation_effect=0
            )
            merchant_instance = Merchant.objects.create(npc=npc)

            items = Item.objects.all()[:5]
            for item in items:
                MerchantInventory.objects.create(
                    merchant=merchant_instance,
                    item=item,
                    quantity=10,
                    price=item.value * 1.5
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded merchants and inventory!"))
