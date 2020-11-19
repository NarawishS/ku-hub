from django import forms
from .models import Blog
from taggit.forms import TagWidget


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter Blog title here'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter short description here'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }
