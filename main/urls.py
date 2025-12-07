from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home),
    path('future/', views.future),
    # path('login/', views.login),
    path('cred/', views.cred),
    path('about/', views.about),
    path('contact/', views.contact),

]