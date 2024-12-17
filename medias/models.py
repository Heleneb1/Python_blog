from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image



class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="media_photos")

    IMAGE_MAX_SIZE = (300, 300)  # Redimensionner l'image en 300x300

    def resize_image(self):
        if self.image:  # Vérifie que l'image existe
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

    def save(self, *args, **kwargs):
        self.resize_image()  # Redimensionne l'image avant de sauvegarder
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption

class Photo_User(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True) # L'utilisateur qui a téléchargé la photo est stocké ici
    
    IMAGE_MAX_SIZE= (300, 300)# Redimensionner l'image en 300x300
    def resize_image(self):
        # Redimensionner l'image
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE) 

        # Enregistrer l'image redimensionnée
        image.save(self.image.path)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return self.caption
    
class Photo_Post(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="uploaded_photos"
    )

    IMAGE_MAX_SIZE = (300, 300)  # Redimensionner l'image en 300x300

    def resize_image(self):
        if self.image:  # Vérifie que l'image existe
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

    def save(self, *args, **kwargs):
        self.resize_image()  # Redimensionne l'image avant de sauvegarder
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption
