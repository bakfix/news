import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import News

@receiver(post_delete, sender=News)
def delete_news_images(sender, instance, **kwargs):
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)