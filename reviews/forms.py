from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = models.Review
        fields = ['kitchen', 'stars', 'comment']
        widgets = {
            'kitchen': forms.Select(attrs={'class': 'form-control'}),
            'stars': forms.Select(
                choices=[(i, f'{i} estrela{'s' if i > 1 else ""}') for i in range(1, 6)],
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'kitchen': 'Cozinha',
            'stars': 'Avaliação',
            'comment': 'Comentário',
        }
