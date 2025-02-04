from rest_framework import viewsets
from space.models import StarSystem, Star, Planet, Moon, SpaceStation, Asteroid, Nebula, UnknownObject
from .serializers import (
    StarSystemSerializer, StarSerializer, PlanetSerializer,
    MoonSerializer, SpaceStationSerializer, AsteroidSerializer,
    NebulaSerializer, UnknownObjectSerializer
)


class StarSystemViewSet(viewsets.ModelViewSet):
    """API endpoint for managing star systems."""
    queryset = StarSystem.objects.all()
    serializer_class = StarSystemSerializer


class StarViewSet(viewsets.ModelViewSet):
    """API endpoint for managing stars."""
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    """API endpoint for managing planets."""
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class MoonViewSet(viewsets.ModelViewSet):
    """API endpoint for managing moons."""
    queryset = Moon.objects.all()
    serializer_class = MoonSerializer


class SpaceStationViewSet(viewsets.ModelViewSet):
    """API endpoint for managing space stations."""
    queryset = SpaceStation.objects.all()
    serializer_class = SpaceStationSerializer


class AsteroidViewSet(viewsets.ModelViewSet):
    """API endpoint for managing asteroids."""
    queryset = Asteroid.objects.all()
    serializer_class = AsteroidSerializer


class NebulaViewSet(viewsets.ModelViewSet):
    """API endpoint for managing nebulas."""
    queryset = Nebula.objects.all()
    serializer_class = NebulaSerializer


class UnknownObjectViewSet(viewsets.ModelViewSet):
    """API endpoint for managing unknown objects."""
    queryset = UnknownObject.objects.all()
    serializer_class = UnknownObjectSerializer
