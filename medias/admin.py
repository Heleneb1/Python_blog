from django.contrib import admin

# Register your models here.
from .models import Photo,Photo_User,Photo_Post

admin.site.register(Photo)
admin.site.register(Photo_User)
admin.site.register(Photo_Post)
# admin.site.register(Message)