from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('kitchen', 'stars', 'created_at')
    search_fields = ('comment', 'kitchen__name')
