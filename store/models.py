import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def wasPublishedRecently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return self.question_text
    
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


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text