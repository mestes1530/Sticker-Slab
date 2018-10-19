from django.db import models
from django.contrib.auth.models import User

class Slab(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    slab_name = models.CharField(max_length=200)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.slab_name