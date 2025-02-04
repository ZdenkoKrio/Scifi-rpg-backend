from rest_framework import viewsets
from .models import Weapon, Armor, Jewelry, QuestItem
from .serializers import WeaponSerializer, ArmorSerializer, JewelrySerializer, QuestItemSerializer
from django.shortcuts import render


def api_overview(request):
    """Render the API overview page for the Items module."""
    return render(request, "api_overview.html")


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
