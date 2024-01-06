from django.urls import path
from .import views

urlpatterns = [
    path('', views.blog, name='home-page'),
    path('newPost/', views.newPost, name='newpost'),
    path('myPost/', views.myPost, name='mypost'),
]