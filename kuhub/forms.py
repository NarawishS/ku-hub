from django import forms
from kuhub.models import Profile


class ExtendProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('display_name', 'profile_pic')

        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
