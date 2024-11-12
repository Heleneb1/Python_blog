from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Photo
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context=context)

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', {'posts': posts})

@login_required
@permission_required('posts.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if 'image' in request.FILES:
                photo = Photo.objects.create(
                    uploader=request.user,
                    image=request.FILES['image'],
                    caption=request.POST.get('caption', '')
                )
        else:
            photo = None
        post = Post.objects.create(title=title, content=content, photo=photo)
        post.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
        return redirect('index')
    return render(request, 'posts/create.html')

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return render(request, 'posts/update_post.html', {'post': post})
        post.title = title
        post.content = content
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post', pk=post.pk)
    return render(request, 'posts/update_post.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('index')
    return render(request, 'posts/delete_post.html', {'post': post})

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
