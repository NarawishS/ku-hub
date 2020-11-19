from django.forms import ModelForm
from django.contrib.auth.models import User
from kuhub.models import Profile


class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)


class ExtendProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)
