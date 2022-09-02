from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings



# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email_serviciu=user.email,
        )




post_save.connect(createProfile, sender=User)