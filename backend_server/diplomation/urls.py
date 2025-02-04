from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactionViewSet, SpeciesViewSet, SpeciesFactionViewSet, api_overview


router = DefaultRouter()
router.register(r"factions", FactionViewSet)
router.register(r"species", SpeciesViewSet)
router.register(r"species-factions", SpeciesFactionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-overview/", api_overview, name="diplomation_api_overview"),
]
