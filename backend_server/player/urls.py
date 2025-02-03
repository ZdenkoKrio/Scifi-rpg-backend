from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PlayerViewSet, PlayerItemViewSet,
    ReputationViewSet, ResistanceViewSet, SkillViewSet
)

router = DefaultRouter()
router.register(r"players", PlayerViewSet)
router.register(r"inventory", PlayerItemViewSet)
router.register(r"reputation", ReputationViewSet)
router.register(r"resistance", ResistanceViewSet)
router.register(r"skills", SkillViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]