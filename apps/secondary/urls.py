from django.urls import path
from apps.secondary import views

urlpatterns = [
    path('blog', views.blog, name = 'blog'),
    path('cart', views.cart, name = 'cart'),
    path('gallery', views.gallery, name = 'gallery'),
    path('grid_sidebar', views.grid_sidebar, name = 'grid_sidebar'),
    path('blog', views.grid_sidebar, name = 'blog'),
    path('member_login', views.member_login, name = 'member_login'),
    path('my_profile', views.my_profile, name = 'my_profile'),
    path('quick_view', views.quick_view, name = 'quick_view'),
    path('single', views.single, name = 'single'),
    path('comand', views.comand, name = 'comand'),
]