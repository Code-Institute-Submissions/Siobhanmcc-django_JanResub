from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog'),
    path('add_post/', views.add_blog_post, name='add_blog_post'),
    
]