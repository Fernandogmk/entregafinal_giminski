
# Register your models here.
from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'author')
    search_fields = ('title', 'subtitle', 'content')
