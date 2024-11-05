from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.contrib import messages
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View



# Create your views here.

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})



def post(request, pk):
     posts = Post.objects.get(id=pk)
     return render(request, 'posts.html', {'posts':posts}) 

def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)

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

class LoginPage(View):
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