from django.db import models
from django.utils import timezone

class RealStateModel(models.Model):
    url = models.URLField(unique=True)
    buy_price = models.DecimalField(max_digits=32, decimal_places=2)
    rent_price = models.DecimalField(max_digits=32, decimal_places=2)
    services_price = models.DecimalField(max_digits=32, decimal_places=2)
    surface = models.DecimalField(max_digits=32, decimal_places=2)
    town = models.CharField(max_length=256)
    raw_data = models.TextField()
    date = models.DateTimeField(default=timezone.now)