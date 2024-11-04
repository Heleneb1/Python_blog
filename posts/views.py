from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.

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
