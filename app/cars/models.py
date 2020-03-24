from django.db import models
from carmanager.models import CarManager


class CarsList(models.Model):
    carmanager = models.ForeignKey(CarManager, on_delete=models.DO_NOTHING)
    vendor = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine = models.CharField(max_length=20)
    fuel_count = models.DecimalField(max_digits=2, decimal_places=1)
    color = models.CharField(max_length=20)
    doors = models.IntegerField()
    seats = models.IntegerField()
    minimum_age = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.vendor
