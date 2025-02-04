from rest_framework import serializers
from .models import StarSystem, Star, Planet, Moon, SpaceStation, Asteroid, Nebula, UnknownObject


class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem
        fields = "__all__"


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = "__all__"


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"


class MoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moon
        fields = "__all__"


class SpaceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceStation
        fields = "__all__"


class AsteroidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asteroid
        fields = "__all__"


class NebulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nebula
        fields = "__all__"


class UnknownObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnknownObject
        fields = "__all__"
