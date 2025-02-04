from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StarSystemViewSet, StarViewSet, PlanetViewSet, MoonViewSet,
    SpaceStationViewSet, AsteroidViewSet, NebulaViewSet, UnknownObjectViewSet, api_overview
)

router = DefaultRouter()
router.register(r'star-systems', StarSystemViewSet)
router.register(r'stars', StarViewSet)
router.register(r'planets', PlanetViewSet)
router.register(r'moons', MoonViewSet)
router.register(r'space-stations', SpaceStationViewSet)
router.register(r'asteroids', AsteroidViewSet)
router.register(r'nebulas', NebulaViewSet)
router.register(r'unknown-objects', UnknownObjectViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-overview/", api_overview, name="space_api_overview"),
]
