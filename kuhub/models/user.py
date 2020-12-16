"""Model create form user getting via signup procedure."""
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """User profile."""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = CloudinaryField('avatar')

    def __str__(self):
        return str(self.user)


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    """Create a new profile for new user."""
    if sociallogin:
        Profile.objects.create(user=user)
