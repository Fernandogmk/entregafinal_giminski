from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject","sender","recipient","sent_at","is_read")
    search_fields = ("subject","body","sender__username","recipient__username")
    list_filter = ("is_read","sent_at")
