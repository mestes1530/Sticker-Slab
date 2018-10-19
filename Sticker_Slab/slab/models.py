from django.db import models
from django.contrib.auth.models import User

class Slab(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StickerType(models.Model):
    type = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.type


class Sticker(models.Model):
    slab = models.ForeignKey(Slab, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(StickerType, on_delete=models.PROTECT)
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return self.name