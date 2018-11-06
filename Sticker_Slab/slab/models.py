from django.db import models
from django.contrib.auth.models import User

class Slab(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    bookmarkings = models.ManyToManyField(User, related_name='bookmarked_slabs', blank=True)
    background = models.ImageField(null=True, blank=True)

    def get_background(self):
        if self.background == '':
            return '/static/slab/images/background_default.jpg'
        return self.background.url

    def __str__(self):
        return self.name


class Sticker(models.Model):
    slab = models.ForeignKey(Slab, on_delete=models.PROTECT)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)
    text = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def is_text(self):
        return self.text is not None and self.text != ''

    def is_link(self):
        return self.link is not None and self.link != ''

    def is_image(self):
        return self.image is not None and self.image != ''

    def get_type(self):
        if self.text is not None or self.text == '':
            return 'text'
        if self.link is not None or self.link == '':
            return 'link'
        return 'image'

    def __str__(self):
        return self.name

class UploadedImages(models.Model):
    sticker_image = models.ImageField(upload_to='images/')
