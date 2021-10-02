from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField("Item Name", max_length=200)
    desc = models.CharField("Descriptions", max_length=200)
    price = models.IntegerField("Item Price")
    image = models.CharField("Image", max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
