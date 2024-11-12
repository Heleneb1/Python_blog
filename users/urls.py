from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
   
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('follow/', views.follow_users, name='follow_users'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/registration/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/registration/password_change_done.html'), name='password_change_done'),
    path('update_profile/', views.update_profile, name='update_profile'),

]
