# Generated by Django 2.1.2 on 2018-11-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slab', '0010_slab_bookmarkings'),
    ]

    operations = [
        migrations.AddField(
            model_name='slab',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
