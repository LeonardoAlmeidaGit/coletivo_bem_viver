from django import forms
from . import models


class MenuForm(forms.ModelForm):

    class Meta:
        model = models.Menu
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }
        labels = {
            'date': 'Data do Cardápio',
        }


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = models.MenuItem
        fields = ['name', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome do Prato',
            'description': 'Descrição',
            'photo': 'Foto do Prato',
        }
