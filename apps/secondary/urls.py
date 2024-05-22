from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('blog', views.blog, name = 'blog'),
    path('gallery', views.gallery, name = 'gallery'),
    path('blog', views.blog, name = 'blog'),
    path('single/<int:id>', views.single, name = 'single'),
    path('comand', views.comand, name = 'comand'),
]