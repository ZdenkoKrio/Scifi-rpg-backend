from rest_framework import serializers
from .models import Faction, Species, SpeciesFaction


class FactionSerializer(serializers.ModelSerializer):
    """Serializer for the Faction model."""
    class Meta:
        model = Faction
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    """Serializer for the Species model."""
    class Meta:
        model = Species
        fields = "__all__"


class SpeciesFactionSerializer(serializers.ModelSerializer):
    """Serializer for the SpeciesFaction model."""
    class Meta:
        model = SpeciesFaction
        fields = "__all__"
