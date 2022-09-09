from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email_serviciu=user.email,
        )


def updateProfile(sender, instance, created, **kwargs):
    if created == False:
        user = instance
        profile = user.profile
        profile.username = user.username
        profile.email_serviciu = user.email
        profile.save()


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=User)
