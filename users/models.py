from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings
from datetime import datetime
from PIL import Image

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
        # Utiliser get_or_create pour garantir l'existence des groupes
        if self.role == self.CREATOR:
            group, created = Group.objects.get_or_create(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group, created = Group.objects.get_or_create(name='subscribers')
            group.user_set.add(self)

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    IMAGE_MAX_SIZE = (300, 300)  # Redimensionner l'image à 300x300

    def resize_image(self):
        try:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)  # Sauvegarder l'image redimensionnée
        except Exception as e:
            print(f"Erreur lors du redimensionnement de l'image: {e}")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return self.caption
