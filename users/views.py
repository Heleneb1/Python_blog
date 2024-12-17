from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.conf import settings

class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue {user.username}')
                return redirect('index')  # Redirige vers l'index après connexion
            else:
                messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect')
        return render(request, self.template_name, context={'form': form})
# TODO revoir le message en cas d'erreur
def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue {user.username}')
                return redirect('index')  # Redirige vers l'index après connexion
            else:
                messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect')
    return render(request, 'users/login.html', context={'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès')  # Message de déconnexion
    return redirect('login')  # Redirige vers la page de connexion

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login après inscription
            messages.success(request, f'Bienvenue, {user.username} ! Votre inscription a été réussie.')
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'users/signup.html', context={'form': form})

def update_profile(request):
    form = forms.ProfileUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès !')
            return redirect('index')
    return render(request, 'users/update_profile.html', context={'form': form})

def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilisateurs suivis avec succès !')
            return redirect('index')
    return render(request, 'users/follow_users.html', context={'form': form})
