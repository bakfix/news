from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text','title')

admin.site.register(News, NewsAdmin)