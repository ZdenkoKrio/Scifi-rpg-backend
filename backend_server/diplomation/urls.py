from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactionViewSet, SpeciesViewSet, SpeciesFactionViewSet


router = DefaultRouter()
router.register(r"factions", FactionViewSet)
router.register(r"species", SpeciesViewSet)
router.register(r"species-factions", SpeciesFactionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
