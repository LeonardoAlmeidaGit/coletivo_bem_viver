from django.contrib import admin
from .models import Kitchen


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ('name', 'neighborhood', 'city', 'contact_person', 'status', 'user')
    search_fields = ('name', 'neighborhood', 'city', 'contact_person', 'user__username')
