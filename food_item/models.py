from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField("Item Name", max_length=200)
    desc = models.CharField("Descriptions", max_length=200)
    price = models.IntegerField("Item Price")
    image = models.CharField("Image", max_length=500)

    def __str__(self):
        return self.name
