from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from kitchens.models import Kitchen


class Review(models.Model):
    kitchen = models.ForeignKey(Kitchen, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Avaliação não pode ser inferior a 1 estrelas'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas'),
        ]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitchen
