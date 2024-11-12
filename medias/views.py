from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Photo


@login_required
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

@login_required(login_url='login')
def photo_view(request):
    photos= Photo.objects.all()

    return render(request, 'photos.html',{'photos':photos})


