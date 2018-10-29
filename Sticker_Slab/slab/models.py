from django.db import models
from django.contrib.auth.models import User

class Slab(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sticker(models.Model):
    slab = models.ForeignKey(Slab, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_type(self):
        if self.text is not None:
            return 'text'
        if self.link is not None:
            return 'link'
        return 'image'

    def __str__(self):
        return self.name

