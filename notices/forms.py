from django import forms
from . import models


class NoticeForm(forms.ModelForm):

    class Meta:
        model = models.Notice
        fields = ['title', 'comment', 'active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Título',
            'comment': 'Comentario',
            'active': 'Status',
        }
