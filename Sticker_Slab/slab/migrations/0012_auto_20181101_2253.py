# Generated by Django 2.1.2 on 2018-11-01 22:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0011_slab_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slab',
            name='bookmarkings',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_slabs', to=settings.AUTH_USER_MODEL),
        ),
    ]
