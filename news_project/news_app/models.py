from django.db import models
from datetime import datetime
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator, MaxValueValidator
from django_admin_geomap import GeoItem

class Category(models.Model):
    name = models.CharField(max_length=50)

class News(models.Model):
    CATEGORY_CHOICES = [
        ('Политика', 'Политика'),
        ('Медицина', 'Медицина'),
        ('Экономика', 'Экономика'),
        ('Общество', 'Общество'),
        ('Культура', 'Культура'),
        ('Спорт', 'Спорт'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Категории')
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    preview_image = models.ImageField(upload_to='news_images/previews/', blank=True, null=True)
    text = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateTimeField(default=datetime.now)
    video = models.FileField(upload_to='news_videos/', null=True, blank=True)  # Добавленное поле


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

        # Создание ContentFile и сохранение его в preview_image
        thumbnail_file = ContentFile(thumbnail_io.getvalue())
        self.preview_image.save(f"preview_{self.main_image.name}", thumbnail_file, save=False)

        # Закрытие буфера
        thumbnail_io.close()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.preview_image:
            # Вызов метода создания превью, если preview_image не установлено
            self.create_thumbnail()
            self.save()  # Повторное сохранение для обновления preview_image

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


