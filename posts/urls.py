from django.urls import path
from . import views



urlpatterns = [
    path('', views.LoginPage.as_view(), name='login'),   # La page de connexion par défaut
    path('index/', views.index, name='index'),  # La page d'accueil après connexion
    path('post/create/', views.add_post, name='create'),
    path('post/<str:pk>/', views.post, name='post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('logout/', views.logout_user, name='logout'),
]
#source C:/Users/Hélène/Documents/Python/python_projects/Envs/blog_env/Scripts/activate
# ou dans le terminal de visual studio code dans le repertoire du projet Documents/Python/python_projects/Envs/blog_env source ./Scripts/activate