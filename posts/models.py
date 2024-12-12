

from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ForeignKey('medias.Photo', on_delete=models.CASCADE, null=True, blank=True, related_name='post_photos')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Nouveau champ pour le créateur
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PostContributor', related_name='contributions')
    
    def __str__(self):
        return self.title

class PostContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('contributor', 'post')

class Photo(models.Model):
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_photos')
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    IMAGE_MAX_SIZE = (300, 300)  # Redimensionner l'image en 300x300

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return self.caption
