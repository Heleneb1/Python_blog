from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views



urlpatterns = [
    # path('', views.LoginPage.as_view(), name='login'),   # La page de connexion par défaut
    path('', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),   # La page de connexion par défaut
    path('index/', views.index, name='index'),  # La page d'accueil après connexion
    path('post/create/', views.add_post, name='create'),
    path('post/<str:pk>/', views.post, name='post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('logout/', views.logout_user, name='logout'),
   # path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('signup/', views.signup_page, name='signup'),
    path('photo/upload/', views.photo_upload, name='photo_upload'),
    path('follow/', views.follow_users, name='follow_users'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Pour servir les fichiers média en mode debug en dev, pour la prod, utiliser un serveur de fichiers statiques comme AWS S3

#source C:/Users/Hélène/Documents/Python/python_projects/Envs/blog_env/Scripts/activate
# ou dans le terminal de visual studio code dans le repertoire du projet Documents/Python/python_projects/Envs/blog_env source ./Scripts/activate