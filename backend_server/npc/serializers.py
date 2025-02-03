from rest_framework import serializers
from .models import NPC
from .models import Merchant, MerchantInventory
from .models import QuestGiver


class NPCSerializer(serializers.ModelSerializer):
    """Serializer for the NPC model."""
    class Meta:
        model = NPC
        fields = "__all__"


class MerchantSerializer(serializers.ModelSerializer):
    """Serializer for the Merchant model."""
    class Meta:
        model = Merchant
        fields = "__all__"


class MerchantInventorySerializer(serializers.ModelSerializer):
    """Serializer for the MerchantInventory model."""
    class Meta:
        model = MerchantInventory
        fields = "__all__"


class QuestGiverSerializer(serializers.ModelSerializer):
    """Serializer for the QuestGiver model."""
    class Meta:
        model = QuestGiver
        fields = "__all__"
