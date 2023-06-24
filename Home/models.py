from django.db import models


# Create your models here.

class Materials(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
    quality = models.CharField(max_length=10)
    image = models.CharField(max_length=10000)
