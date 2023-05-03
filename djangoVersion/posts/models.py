from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField(primary_key=True, unique=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    transaction_type = models.CharField(max_length=10)
    transaction_location = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    image = models.ImageField()