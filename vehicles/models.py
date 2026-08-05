from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=30)
    purchase_date = models.DateField()

    def __str__(self):
        return self.vehicle_number