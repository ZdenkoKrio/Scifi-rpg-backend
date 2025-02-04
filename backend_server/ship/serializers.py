from rest_framework import serializers
from .models import Ship, ShipArmor, ShipWeapon, ShipUpgrade, ShipCrew


class ShipSerializer(serializers.ModelSerializer):
    """Serializer for the Ship model."""
    class Meta:
        model = Ship
        fields = "__all__"


class ShipArmorSerializer(serializers.ModelSerializer):
    """Serializer for the ShipArmor model."""
    class Meta:
        model = ShipArmor
        fields = "__all__"


class ShipWeaponSerializer(serializers.ModelSerializer):
    """Serializer for the ShipWeapon model."""
    class Meta:
        model = ShipWeapon
        fields = "__all__"


class ShipUpgradeSerializer(serializers.ModelSerializer):
    """Serializer for the ShipUpgrade model."""
    class Meta:
        model = ShipUpgrade
        fields = "__all__"


class ShipCrewSerializer(serializers.ModelSerializer):
    """Serializer for the ShipCrew model."""
    class Meta:
        model = ShipCrew
        fields = "__all__"
