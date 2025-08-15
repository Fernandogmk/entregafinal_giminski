# blog/forms.py
from django import forms
from django.forms import ClearableFileInput
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'published_at', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'published_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': ' '}),
            #'image': ClearableFileInput(attrs={'class': 'form-control'}),  # << acá
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            # si no usás CKEditor:
            # 'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
        labels = {
            'title': 'Title',
            'subtitle': 'Subtitle',
            'published_at': 'Published at',
            'image': 'Image',
            'content': 'Content',
        }
