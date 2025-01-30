from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
