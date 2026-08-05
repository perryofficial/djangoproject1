from django.db import models

# Create your models here.
class Inventory(models.Model):
    item_name= models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name