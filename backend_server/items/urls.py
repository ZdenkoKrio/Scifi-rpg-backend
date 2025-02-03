from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeaponViewSet, ArmorViewSet, JewelryViewSet, QuestItemViewSet


router = DefaultRouter()
router.register(r'weapons', WeaponViewSet)
router.register(r'armors', ArmorViewSet)
router.register(r'jewelry', JewelryViewSet)
router.register(r'quest-items', QuestItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
