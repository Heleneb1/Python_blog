from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>/', views.post, name='post'),
    path('create/', views.add_post, name='create'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/update/', views.update_post, name='update_post')
    
]