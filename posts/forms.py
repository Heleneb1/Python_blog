
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'role']
        exclude = ['password']


class PhotoForm(forms.ModelForm):
    class Meta:
        model= models.Photo
        fields = ['image', 'caption']

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['follows']

from django import forms
from .models import Post, Photo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photos']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Saisis ton contenu en Markdown...'}),
        }
