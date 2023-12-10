from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import News, Place
from django_admin_geomap import ModelAdmin

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', 'title')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'rating')
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Place, ModelAdmin)
