from django import forms
from . import models


class KitchenForm(forms.ModelForm):

    class Meta:
        model = models.Kitchen
        fields = ['name', 'address', 'neighborhood', 'city', 'phone', 'opening_hours', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_hours': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome da Cozinha',
            'address': 'Endereço',
            'neighborhood': 'Bairro',
            'city': 'Cidade',
            'phone': 'Telefone',
            'opening_hours': 'Horários de Funcionamento',
            'description': 'Descrição',
            'photo': 'Foto da Cozinha',
        }
