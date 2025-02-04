from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ShipViewSet, ShipArmorViewSet, ShipWeaponViewSet,
    ShipUpgradeViewSet, ShipCrewViewSet
)

router = DefaultRouter()
router.register(r"ships", ShipViewSet)
router.register(r"ship-armor", ShipArmorViewSet)
router.register(r"ship-weapons", ShipWeaponViewSet)
router.register(r"ship-upgrades", ShipUpgradeViewSet)
router.register(r"ship-crew", ShipCrewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
