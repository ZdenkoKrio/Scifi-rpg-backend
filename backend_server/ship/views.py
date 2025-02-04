from rest_framework import viewsets
from .models import Ship, ShipArmor, ShipWeapon, ShipUpgrade, ShipCrew
from .serializers import (
    ShipSerializer, ShipArmorSerializer, ShipWeaponSerializer,
    ShipUpgradeSerializer, ShipCrewSerializer
)


class ShipViewSet(viewsets.ModelViewSet):
    """API endpoint for managing ships."""
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer


class ShipArmorViewSet(viewsets.ModelViewSet):
    """API endpoint for managing ship armor."""
    queryset = ShipArmor.objects.all()
    serializer_class = ShipArmorSerializer


class ShipWeaponViewSet(viewsets.ModelViewSet):
    """API endpoint for managing ship weapons."""
    queryset = ShipWeapon.objects.all()
    serializer_class = ShipWeaponSerializer


class ShipUpgradeViewSet(viewsets.ModelViewSet):
    """API endpoint for managing ship upgrades."""
    queryset = ShipUpgrade.objects.all()
    serializer_class = ShipUpgradeSerializer


class ShipCrewViewSet(viewsets.ModelViewSet):
    """API endpoint for managing ship crew."""
    queryset = ShipCrew.objects.all()
    serializer_class = ShipCrewSerializer
