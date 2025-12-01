from django.db import models
from django.conf import settings
from django.utils import timezone



# python -m pip install markdown2 hors venv
import markdown2




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
        content_convert = markdown2.markdown(self.content, extras=['fenced-code-blocks', 'tables'])
        return content_convert
    def __str__(self):
        return self.title



class PostContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('contributor', 'post')
        verbose_name_plural = 'Post Contributors'