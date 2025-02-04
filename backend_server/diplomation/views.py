from rest_framework import viewsets
from .models import Faction, Species, SpeciesFaction
from .serializers import FactionSerializer, SpeciesSerializer, SpeciesFactionSerializer


class FactionViewSet(viewsets.ModelViewSet):
    """API endpoint for managing factions."""
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """API endpoint for managing species."""
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class SpeciesFactionViewSet(viewsets.ModelViewSet):
    """API endpoint for managing species-faction relationships."""
    queryset = SpeciesFaction.objects.all()
    serializer_class = SpeciesFactionSerializer
    