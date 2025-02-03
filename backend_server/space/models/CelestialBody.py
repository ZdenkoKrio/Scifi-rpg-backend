class CelestialBody(models.Model):
    """Abstract base model for all celestial bodies (planets, asteroids, stations)."""
    name = models.CharField(max_length=100)
    star_system = models.ForeignKey(StarSystem, on_delete=models.CASCADE, related_name="bodies")
    size = models.IntegerField()  # General size metric
    composition = models.CharField(max_length=100, blank=True)  # Rock, gas, metal
    resource_richness = models.IntegerField(default=0)  # Resource value (0 = barren, 100 = rich)

    class Meta:
        abstract = True  # This makes CelestialBody an abstract model

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"
    