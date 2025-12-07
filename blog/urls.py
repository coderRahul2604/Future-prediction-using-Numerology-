from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_post, name='create_post'),
    
]