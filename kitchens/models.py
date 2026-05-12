from django.db import models
from users.models import User


class Kitchen(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='kitchen')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='kitchens/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    opening_hours = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
