from rest_framework import serializers
from .models import Player, PlayerItem, Reputation, Resistance, Skill


class PlayerSerializer(serializers.ModelSerializer):
    """Serializer for the Player model."""
    user = serializers.StringRelatedField()  # Zobrazenie mena používateľa

    class Meta:
        model = Player
        fields = "__all__"


class PlayerItemSerializer(serializers.ModelSerializer):
    """Serializer for the PlayerItem model."""
    class Meta:
        model = PlayerItem
        fields = "__all__"


class ReputationSerializer(serializers.ModelSerializer):
    """Serializer for the Reputation model."""
    class Meta:
        model = Reputation
        fields = "__all__"


class ResistanceSerializer(serializers.ModelSerializer):
    """Serializer for the Resistance model."""
    class Meta:
        model = Resistance
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Serializer for the Skill model."""
    class Meta:
        model = Skill
        fields = "__all__"
