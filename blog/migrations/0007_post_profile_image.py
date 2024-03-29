# Generated by Django 4.2.10 on 2024-03-04 12:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
