from django.db import models
from datetime import datetime
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator, MaxValueValidator
from django_admin_geomap import GeoItem
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE,
                             related_name='comments')  # Используйте строку 'News' вместо имени класса
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.news.title}'


class News(models.Model):
    CATEGORY_CHOICES = [
        ('Политика', 'Политика'),
        ('СВО', 'СВО'),
        ('Экономика', 'Экономика'),
        ('Общество', 'Общество'),
        ('Медицина', 'Медицина'),
        ('Культура', 'Культура'),
        ('Спорт', 'Спорт'),

    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Категории')
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    text = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField(default=datetime.now)
    video = models.FileField(upload_to='news_videos/', null=True, blank=True)  # Добавленное поле
    CITY_CHOICES = [
        ('СВО', 'СВО'),
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Новосибирск', 'Новосибирск'),
        ('Красноярск', 'Красноярск'),
        ('Кемерово', 'Кемерово'),
        ('Краснодар', 'Краснодар'),
        ('Хабаровск', 'Хабаровск'),
    ]
    city = models.CharField(max_length=100, choices=CITY_CHOICES, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    DURATION_CHOICES = (
        (3, '3 месяца'),
        (6, '6 месяцев'),
        (12, '12 месяцев'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    duration = models.IntegerField(choices=DURATION_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.duration} месяцев'


class FavoriteNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def create_thumbnail(self):
        img = Image.open(self.main_image.path)
        img = ImageOps.exif_transpose(img)
        img = img.convert('RGB')

        # Определение новых размеров
        base_width = 200
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))

        # Создание превью
        thumbnail = img.resize((base_width, h_size), Image.LANCZOS)

        # Сохранение превью в ContentFile
        thumbnail_io = BytesIO()
        thumbnail.save(thumbnail_io, format='JPEG')

        # Закрытие буфера
        thumbnail_io.close()

    def __str__(self):
        return self.title


# places/models.py
class Place(models.Model, GeoItem):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(25)])

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    def __str__(self):
        return self.name
