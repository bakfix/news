from rest_framework import serializers
from .models import News, City

class NewsSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())

    class Meta:
        model = News
        fields = ['category', 'title', 'main_image', 'text', 'author', 'publication_date', 'video', 'city']
