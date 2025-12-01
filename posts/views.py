import logging
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from medias.models import Photo_Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
import markdown2

import markdown2



def index(request):
    posts = Post.objects.all().order_by('-created_at')
    # Ajouter une conversion en HTML tronqué pour chaque post
    for post in posts:
        post.converted_content = ' '.join(post.content.split()[:20]) + '...'  # Tronquer le contenu
        post.converted_content = markdown2.markdown(post.converted_content)  # Convertir en HTML

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context=context)


def post(request, pk):
    post_instance = get_object_or_404(Post, id=pk)
    convert_content = post_instance.content_as_html()
    return render(request, 'posts/post.html', {'post': post_instance, 'convert_content': convert_content})

    # convert_content = markdown2.markdown(post_instance.content)
    # return render(request, 'posts/post.html', {'post': post_instance, 'convert_content': convert_content})


@login_required
@permission_required('posts.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        photo_file = request.FILES.get('photo')

        # Vérifie si une photo avec le même nom existe déjà dans Photo_Post
        if photo_file:
            photo_instance = Photo_Post.objects.filter(image=photo_file.name).first()

            # Si aucune photo existante n'est trouvée, crée une nouvelle photo
            if not photo_instance:
                photo_instance = Photo_Post.objects.create(
                    image=photo_file,
                    uploader=request.user,
                    caption=photo_file.name
                )
            logging.info(f"Photo uploadée : {photo_file.name if photo_file else 'Aucune photo'}")

        # Crée un post avec la photo optionnelle
        post = Post.objects.create(
            title=title,
            content=content,
            photos=photo_instance if photo_file else None,  # Associe la photo ou None
            creator=request.user,
            created_at=timezone.now()
        )

        # Ajoute l'utilisateur comme contributeur
        post.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})

        return redirect('index')

    return render(request, 'posts/create.html')

@user_passes_test(lambda u: u.is_authenticated)
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        photo_file = request.FILES.get('photo')
        if not title or not content:
            messages.error(request, 'Title and content are required.')
            return render(request, 'posts/update_post.html', {'post': post})
        post.title = title
        post.content = content
        # Si une photo est téléchargée, on la met à jour
        if photo_file:
            post.photos.image = photo_file  # Met à jour l'image associée au post
            post.photos.save()  # Sauvegarde le modèle Photo_Post avec la nouvelle image

        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post', pk=post.pk)
    return render(request, 'posts/update_post.html', {'post': post})

@user_passes_test(lambda u: u.is_superuser)
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
