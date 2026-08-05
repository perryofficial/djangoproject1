from django.db import models

# Create your models here.
class Clothes(models.Model):
    item_name= models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.item_id