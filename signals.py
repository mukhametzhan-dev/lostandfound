from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import Group
# from .models import StaffProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



@receiver(post_save, sender=StaffProfile)
def assign_staff_group(sender, instance, created, **kwargs):
    if created:
        staff_group, _ = Group.objects.get_or_create(name='Staff')
        instance.user.groups.add(staff_group)
