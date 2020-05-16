from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('profile/<username>', views.profile, name='profile'),
    path('category/<category>', views.category, name='category'),
    path('likes', views.liked_post, name='like-quotes'),
    path('blog/<slug>', views.single, name='single'),
    path('createblog', views.create_blog, name='createblog'),
]
