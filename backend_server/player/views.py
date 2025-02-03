from rest_framework import viewsets
from .models import Player, PlayerItem, Reputation, Resistance, Skill
from .serializers import (
    PlayerSerializer, PlayerItemSerializer,
    ReputationSerializer, ResistanceSerializer, SkillSerializer
)


class PlayerViewSet(viewsets.ModelViewSet):
    """API endpoint for managing players."""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerItemViewSet(viewsets.ModelViewSet):
    """API endpoint for managing player inventory."""
    queryset = PlayerItem.objects.all()
    serializer_class = PlayerItemSerializer


class ReputationViewSet(viewsets.ModelViewSet):
    """API endpoint for managing player reputations."""
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer


class ResistanceViewSet(viewsets.ModelViewSet):
    """API endpoint for managing player resistances."""
    queryset = Resistance.objects.all()
    serializer_class = ResistanceSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """API endpoint for managing player skills."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    