from django.db import models
from kitchens.models import Kitchen


class Notice(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.PROTECT, related_name='notices')
    title = models.CharField(max_length=100)
    comment = models.TextField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
