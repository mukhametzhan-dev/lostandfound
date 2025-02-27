from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.FileField()
    # found = models.BooleanField(default=False)
    found_by = models.CharField(max_length=150, blank=True, null=True)
    contact_info = models.CharField(max_length=255)
    creator_username = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])


class Usr(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return f"{self.user_id}: {self.username}"


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   # image = models.ImageField(default='default.png', upload_to='profile_pics', null=True,  blank=True)
    image = models.FileField(default='default.png', upload_to='profile_pics', null=True, blank=True)

    def str(self):
        return f'{self.user.username} Profile'
