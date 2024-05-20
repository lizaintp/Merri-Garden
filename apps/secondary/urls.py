from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('blog', views.blog, name = 'blog'),
    path('gallery', views.gallery, name = 'gallery'),
    path('blog', views.blog, name = 'blog'),
    path('comand', views.comand, name = 'comand'),
    path('single', views.single, name = 'single'),
]