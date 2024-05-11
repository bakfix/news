from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import News, Place
from .models import Subscription

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', 'title')


class PlaceAdmin(admin.ModelAdmin):  # Исправлено: использовать admin.ModelAdmin
    list_display = ('name', 'latitude', 'longitude', 'rating')
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Place, PlaceAdmin)  # Исправлено: заменено ModelAdmin на PlaceAdmin
admin.site.register(Subscription)