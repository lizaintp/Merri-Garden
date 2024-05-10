from django.urls import path
from apps.secondary.views import blog, portfolio_page, portfolio, post, services_page, services

urlpatterns = [
    path('blog', blog, name = 'blog'),
    path('portfolio-page', portfolio_page, name = 'portfolio-page'),
    path('portfolio', portfolio, name = 'portfolio'),
    path('post', post, name = 'post'),
    path('services-page', services_page, name = 'services-page'),
    path('services', services, name = 'services'),
]