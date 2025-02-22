from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NPCViewSet, MerchantViewSet, MerchantInventoryViewSet, QuestGiverViewSet, api_overview


router = DefaultRouter()
router.register(r"npcs", NPCViewSet)
router.register(r"merchants", MerchantViewSet)
router.register(r"merchant-inventory", MerchantInventoryViewSet)
router.register(r"quest-givers", QuestGiverViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-overview/", api_overview, name="npc_api_overview"),
]
