from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add_post, name='create'),
    path('<int:pk>/', views.post, name='post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('<int:pk>/update/', views.update_post, name='update_post'),
    path('search/', views.search, name='search'),
]
