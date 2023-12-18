# Ваш файл apps.py в директории news_app
from django.apps import AppConfig

class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_app'

    def ready(self):
        from news_app.signals import delete_news_images
