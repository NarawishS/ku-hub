from django.forms import ModelForm
from kuhub.models import Profile


class ExtendProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('display_name', 'profile_pic')
