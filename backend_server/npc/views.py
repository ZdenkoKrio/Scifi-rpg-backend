from rest_framework import viewsets
from .models import NPC, Merchant, MerchantInventory, QuestGiver
from .serializers import NPCSerializer, MerchantSerializer, MerchantInventorySerializer, QuestGiverSerializer


class NPCViewSet(viewsets.ModelViewSet):
    """API endpoint for NPCs."""
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer


class MerchantViewSet(viewsets.ModelViewSet):
    """API endpoint for Merchants."""
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantInventoryViewSet(viewsets.ModelViewSet):
    """API endpoint for Merchant Inventory."""
    queryset = MerchantInventory.objects.all()
    serializer_class = MerchantInventorySerializer


class QuestGiverViewSet(viewsets.ModelViewSet):
    """API endpoint for Quest Givers."""
    queryset = QuestGiver.objects.all()
    serializer_class = QuestGiverSerializer
