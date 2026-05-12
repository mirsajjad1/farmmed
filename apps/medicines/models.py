from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    purchase_price = models.FloatField()
    
    def __str__(self):
        return self.name