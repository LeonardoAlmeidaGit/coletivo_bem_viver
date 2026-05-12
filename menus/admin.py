from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('kitchen', 'date', 'active', 'created_at')
    search_fields = ('kitchen__name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'created_at')
    search_fields = ('name', 'menu__kitchen__name')
