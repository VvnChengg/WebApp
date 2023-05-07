from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(auto_created=True, primary_key=True)
    # user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    transaction_type = models.CharField(max_length=20)
    transaction_location = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')