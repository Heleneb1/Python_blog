from django.db import models
from django.contrib.auth.models import AbstractUser,Group


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = [
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    ]
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=300, choices=ROLE_CHOICES, default=SUBSCRIBER)
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)


