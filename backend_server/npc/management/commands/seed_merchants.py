from django.core.management.base import BaseCommand
from npc.models import NPC, Merchant, MerchantInventory
from items.models import Weapon, Armor, Jewelry, QuestItem
from diplomation.models import Faction


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
            faction, _ = Faction.objects.get_or_create(
                name=merchant["faction"],
                defaults={"description": f"Faction {merchant['faction']} description"}
            )

            npc = NPC.objects.create(
                name=merchant["name"],
                role="merchant",
                level=3,
                faction=faction,
                dialogue="Looking for the best deals in the galaxy?",
                reputation_effect=0
            )
            merchant_instance = Merchant.objects.create(npc=npc)

            items = list(Weapon.objects.all()[:2]) + list(Armor.objects.all()[:1]) + list(Jewelry.objects.all()[:1]) + list(QuestItem.objects.all()[:1])

            if not items:
                self.stdout.write(self.style.WARNING(f"No items found for merchant {merchant['name']}"))

            for item in items:
                MerchantInventory.objects.create(
                    merchant=merchant_instance,
                    item=item,
                    quantity=10,
                    price=item.value * 1.5
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded merchants and inventory!"))