from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sounds/', views.sounds, name='sounds'),
    path('profile/', views.user_profile, name='profile'),
    path('users_mixes/', views.other_users_mixes, name='users_mixes'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
