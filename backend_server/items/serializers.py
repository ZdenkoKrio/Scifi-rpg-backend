from rest_framework import serializers
from .models import Weapon, Armor, Jewelry, QuestItem


class WeaponSerializer(serializers.ModelSerializer):
    """Serializer for the Weapon model."""
    class Meta:
        model = Weapon
        fields = "__all__"


class ArmorSerializer(serializers.ModelSerializer):
    """Serializer for the Armor model."""
    class Meta:
        model = Armor
        fields = "__all__"


class JewelrySerializer(serializers.ModelSerializer):
    """Serializer for the Jewelry model."""
    class Meta:
        model = Jewelry
        fields = "__all__"


class QuestItemSerializer(serializers.ModelSerializer):
    """Serializer for the QuestItem model."""
    class Meta:
        model = QuestItem
        fields = "__all__"
