from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signals are used here because we have two apps (users and projectunit).
# These signals help coordinate CRUD operations between our apps, and ensure parallelism.

# Signal for creating profile. Links User with Profile object. 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal for updating profile. Links User with updated Profile object.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
