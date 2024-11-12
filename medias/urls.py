from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.photo_upload, name='photo_upload'),
    path('photos/', views.photo_view, name='photo_view'),  # Route pour afficher les photos
]
