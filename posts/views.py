from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostContributor, Photo
from django.http import HttpResponse
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import View
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator




# Create your views here.

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all().order_by('-created_at') # Récupère tous les posts et les trie par date de création
    paginator = Paginator(posts, 4)  # Affiche 4 posts par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context=context)




def post(request, pk): #permet de voir un post en particulier
     posts = Post.objects.get(id=pk)
     return render(request, 'posts.html', {'posts':posts}) 

@login_required
@permission_required('posts.add_post', raise_exception=True) # Vérifie si l'utilisateur a la permission d'ajouter un post et raise_exception=True pour renvoyer une erreur 403 si l'utilisateur n'a pas la permission
@login_required
@permission_required('posts.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        photo_file = request.FILES.get('photo')

        # Créer la photo si elle existe
        if photo_file:
            photo = Photo.objects.create(image=photo_file, uploader=request.user)
        else:
            photo = None  # Pas de photo téléchargée

        # Créer le post avec la photo et l'auteur
        post = Post.objects.create(
            title=title,
            content=content,
            photo=photo,
           
        )

        # Ajouter le contributeur (l'auteur principal) au post
        post.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})

        return redirect('index')
    return render(request, 'create.html', {'message': 'Post added successfully!'})
    
def update_post(request, pk):
    """Met à jour un post existant."""
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return render(request, 'update_post.html', {'post': post})
            
        post.title = title
        post.content = content
        post.save()
        
        messages.success(request, 'Post updated successfully!')
        return redirect('post', pk=post.pk)
        
    return render(request, 'update_post.html', {'post': post})
# def delete_post(request, pk):
#     post = Post.objects.get(id=pk)
#     post.delete()
#     return HttpResponse('Post deleted successfully!')

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')  # Message de succès
        return redirect('index')
    return render(request, 'delete_post.html', {'post': post})

   

class LoginPage(View): # Vue basée sur une classe
    form_class = forms.LoginForm
    template_name = 'login.html'
    def get(self, request):
        form = self.form_class()
        message =''
        return render(request, self.template_name, context={'form': form})


    

    def post(self, request):
        message = ""
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

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        message = "Veuillez vous connecter pour accéder au contenu."
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                
                login(request, user)
                messages.success(request, f'Bienvenue {user.username}')
                return redirect('index')  # Redirige vers l'index après connexion
            else:
                messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect')
    
    return render(request, 'login.html', context={'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès')  # Utilise messages pour le message de déconnexion
    return redirect('login')  # Redirige vers la page de connexion

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save()
            # Auto-login après inscription
            login(request, user)
            messages.success(request, f'Bienvenue, {user.username} ! Votre inscription a été réussie.')
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', context={'form': form})


def update_profile(request):
    form = forms.ProfileUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès !')
            return redirect('index')
    return render(request, 'update_profile.html', context={'form': form})

def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilisateurs suivis avec succès !')
            return redirect('index')
    return render(request, 'follow_users.html', context={'form': form})

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



# def search(request):
#     query = request.GET.get('q') # Récupère la requête de recherche
#     posts = Post.objects.filter(
#         Q(title__icontains=query) | Q(content__icontains=query) # Recherche dans le titre et le contenu
#     )
#     return render(request, 'index.html', {'posts': posts})

def search(request):
    query = request.GET.get('q')  # Récupère la requête de recherche
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)  # Recherche dans le titre et le contenu
    ).order_by('-created_at')  # Tri les résultats par date de création

    paginator = Paginator(posts, 4)  # Affiche 4 résultats par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'query': query}
    return render(request, 'index.html', context)
