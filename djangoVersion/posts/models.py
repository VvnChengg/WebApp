from django.db import models

# Create your models here.
class Item(models.Model):
    # item_id = models.IntegerField(primary_key=True, unique=True)
    # user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    # TYPE = (
    #     ("僅面交"),
    #     ("僅寄送"),
    #     ("面交、寄送皆可"),
    # )
    transaction_type = models.CharField(max_length=20)

    transaction_location = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField()

    # CAT = (
    #     ("衣物"),
    #     ("鞋子"),
    #     ("3C"),
    #     ("其他"),
    # )
    category = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    image = models.ImageField()