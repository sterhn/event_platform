from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        role = instance.profile.role  # Get the role from the user instance
        user_profile.role = role  # Set the role for the UserProfile
        user_profile.save()  # Save the UserProfile
