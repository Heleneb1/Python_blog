from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'  
    ROLE_CHOICES = [
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),  
    ]
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=300, choices=ROLE_CHOICES, default=SUBSCRIBER)

# Pour créer un utilisateur, ouvrez un terminal et exécutez les commandes suivantes:

#     $ py manage.py shell
# Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from posts.models import User
# >>> User.objects.create_user(username='toto', password='S3cret!', role='CREATOR')
# <User: toto>
#exit() pour quitter le shell
