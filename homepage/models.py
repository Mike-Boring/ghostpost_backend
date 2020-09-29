from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils import timezone
# Create your models here.


class MyUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class BoastsRoasts(models.Model):
    post_choices = (
        ('boast', 'Boast'),
        ('roast', 'Roast'),
    )
    post_type = models.CharField(
        max_length=32, choices=post_choices, unique=True, default='Boast')
    boasts = models.BooleanField(default=True)
    post_text = models.CharField(max_length=240)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_text
