from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.conf import settings
from django.utils import timezone
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
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)


# Pour créer un utilisateur, ouvrez un terminal et exécutez les commandes suivantes:

#     $ py manage.py shell
# Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from posts.models import User
# >>> User.objects.create_user(username='toto', password='S3cret!', role='CREATOR')
# <User: toto>
#exit() pour quitter le shell

# class Photo_User(models.Model):
#     image = models.ImageField(upload_to='photos/')
#     caption = models.CharField(max_length=300)
#     created_at = models.DateTimeField(default=timezone.now, blank=True)
#     uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) # L'utilisateur qui a téléchargé la photo est stocké ici
    
#     IMAGE_MAX_SIZE= (300, 300)# Redimensionner l'image en 300x300
#     def resize_image(self):
#         # Redimensionner l'image
#         image = Image.open(self.image)
#         image.thumbnail(self.IMAGE_MAX_SIZE) 

#         # Enregistrer l'image redimensionnée
#         image.save(self.image.path)
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         self.resize_image()

#     def __str__(self):
#         return self.caption