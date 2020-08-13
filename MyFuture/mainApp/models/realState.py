from django.db import models
from django.utils import timezone

class RealStateModel(models.Model):
    url = models.URLField(unique=True)

    buy_price = models.DecimalField(max_digits=32, decimal_places=2, null=True)
    buy_currency = models.CharField(max_length=256, null=True)
    rent_price = models.DecimalField(max_digits=32, decimal_places=2, null=True)
    rent_currency = models.CharField(max_length=256, null=True)
    expenses_price = models.DecimalField(max_digits=32, decimal_places=2, null=True)
    expenses_currency = models.CharField(max_length=256, null=True)

    total_square_meters = models.DecimalField(max_digits=32, decimal_places=2, null=True)
    covered_square_meters = models.DecimalField(max_digits=32, decimal_places=2, null=True)
    number_of_rooms = models.SmallIntegerField(null=True)
    address = models.CharField(max_length=256, null=True)
    town = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=256, default='argentina')

    raw_data = models.TextField()
    date = models.DateTimeField(default=timezone.now)
