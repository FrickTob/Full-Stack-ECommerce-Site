import datetime
from django.db import models
from django.utils import timezone

    
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(null=True, upload_to="./")

    def isInStock(self):
        return self.product_quantity > 0
    
    def __str__(self) -> str:
        return self.product_title
