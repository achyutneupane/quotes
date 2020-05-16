from django import forms
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'main_menu',
                   'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'main_menu': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
