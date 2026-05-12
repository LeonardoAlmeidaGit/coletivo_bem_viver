from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'kitchen', 'active', 'created_at')
    search_fields = ('title', 'comment', 'kitchen__name')
