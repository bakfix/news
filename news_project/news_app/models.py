from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    preview_image = models.ImageField(upload_to='news_images/previews/', blank=True, null=True)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.preview_image:
            self.preview_image = self.generate_preview_image()
        super().save(*args, **kwargs)

    def generate_preview_image(self):
        # Реализуйте генерацию превью-изображения здесь (пример: использование PIL)
        # Обратитесь к документации для работы с изображениями в Django
        pass
