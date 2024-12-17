from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from . import forms
from .models import Photo
from medias.models import Photo_Post, Photo_User


@user_passes_test(lambda u: u.is_superuser)
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo =form.save(commit=False) # commit=False pour éviter l'enregistrement automatique
            photo.uploader = request.user
            photo.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('index')
    return render(request, 'photo_upload.html', context={'form': form})

@user_passes_test(lambda u: u.is_superuser)
def photo_view(request):

    photos = Photo.objects.all()
    photo_users = Photo_User.objects.all()
    photo_posts = Photo_Post.objects.all()

    context = {
        'photos': photos,
        'photo_users': photo_users,
        'photo_posts': photo_posts,
    }
    return render(request, 'photos.html', context)



