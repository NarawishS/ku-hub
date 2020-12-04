from django import forms
from kuhub.models import Blog, Profile
from taggit.forms import TagWidget
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_description', 'body', 'tags', 'forum', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter Blog title here'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter short description here'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ExtendProfileForm(forms.ModelForm):
    profile_pic = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'avatars'
       }
    )
    class Meta:
        model = Profile
        fields = ('display_name', 'profile_pic')

        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
