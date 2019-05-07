from django.contrib import admin
from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name='user-reg'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='user-login'),
    path('profile/', user_views.profile, name='user-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='user-logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

]
