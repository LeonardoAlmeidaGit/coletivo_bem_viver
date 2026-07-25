from django.db import models
from kitchens.models import Kitchen


class Menu(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.PROTECT, related_name='menus')
    date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kitchen.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='menu_items')
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='menus/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
