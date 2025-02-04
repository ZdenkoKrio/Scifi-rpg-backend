from rest_framework import viewsets
from django.apps import apps
from .serializers import WeaponSerializer, ArmorSerializer, JewelrySerializer, QuestItemSerializer
from django.shortcuts import render

Weapon = apps.get_model("items", "Weapon")
Armor = apps.get_model("items", "Armor")
Jewelry = apps.get_model("items", "Jewelry")
QuestItem = apps.get_model("items", "QuestItem")


def api_overview(request):
    """Render the API overview page for the Items module."""
    return render(request, "items/api_overview.html")


class WeaponViewSet(viewsets.ModelViewSet):
    """API endpoint that allows weapons to be viewed or edited."""
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class ArmorViewSet(viewsets.ModelViewSet):
    """API endpoint that allows armors to be viewed or edited."""
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class JewelryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows jewelry to be viewed or edited."""
    queryset = Jewelry.objects.all()
    serializer_class = JewelrySerializer


class QuestItemViewSet(viewsets.ModelViewSet):
    """API endpoint that allows quest items to be viewed or edited."""
    queryset = QuestItem.objects.all()
    serializer_class = QuestItemSerializer
