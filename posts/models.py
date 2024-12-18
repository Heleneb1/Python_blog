from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group


# python -m pip install markdown hors venv    
import markdown2

from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photos = models.ForeignKey('medias.Photo_Post', on_delete=models.CASCADE, null=True, blank=True, related_name='post_photos')
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    creator = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    on_delete=models.SET_NULL, 
    null=True,  # Keep null=True if you want to allow posts without a specific creator
    blank=False,  # Prevents blank values in forms
    related_name='created_posts'
)
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_posts')
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PostContributor', related_name='contributions')


    def content_as_html(self):
        """Convertir le contenu Markdown en HTML"""
        convert_content = markdown2.markdown(self.content, extras=['fenced-code-blocks', 'tables', 'highlighting'])
        return convert_content 
    def __str__(self):
        return self.title
    


class PostContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('contributor', 'post')
        verbose_name_plural = 'Post Contributors'

# class Photo_Post(models.Model):
#     photo_post = models.ImageField(null=True, upload_to='photos_post/')
#     caption = models.CharField(max_length=300)
#     created_at = models.DateTimeField(default=timezone.now, blank=True)
#     uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="uploaded_photos")

#     IMAGE_MAX_SIZE = (300, 300)  # Redimensionner l'image en 300x300

#     def resize_image(self):
#         if self.photo_post:  # Vérifie que l'image existe
#             image = Image.open(self.photo_post)
#             image.thumbnail(self.IMAGE_MAX_SIZE)
#             image.save(self.photo_post.path)

#     def save(self, *args, **kwargs):
#         self.resize_image()  # Redimensionne l'image avant de sauvegarder
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.caption
