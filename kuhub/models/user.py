from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return str(self.user)


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    if sociallogin:
        Profile.objects.create(user=user)
