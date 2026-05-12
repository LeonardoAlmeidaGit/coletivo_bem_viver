from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_superuser', 'get_kitchen')

    def get_kitchen(self, obj):
        try:
            return obj.kitchen.name
        except Exception:
            return 'Sem cozinha vinculada'

    get_kitchen.short_description = 'Cozinha'
