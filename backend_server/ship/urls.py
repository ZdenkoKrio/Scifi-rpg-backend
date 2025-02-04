from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ShipViewSet, ShipArmorViewSet, ShipWeaponViewSet,
    ShipUpgradeViewSet, ShipCrewViewSet, api_overview
)

router = DefaultRouter()
router.register(r"ships", ShipViewSet)
router.register(r"ship-armor", ShipArmorViewSet)
router.register(r"ship-weapons", ShipWeaponViewSet)
router.register(r"ship-upgrades", ShipUpgradeViewSet)
router.register(r"ship-crew", ShipCrewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-overview/", api_overview, name="ship_api_overview"),
]
