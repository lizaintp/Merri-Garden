from django.urls import path
from apps.secondary.views import blog, courses, single_blog, single_course, comand, comand_profile

urlpatterns = [
    path('blog', blog, name = 'blog'),
    path('courses', courses, name = 'courses'),
    path('single_blog', single_blog, name = 'single_blog'),
    path('single_course', single_course, name = 'single_course'),
    path('comand', comand, name = 'comand'),
    path('comand_profile', comand_profile, name = 'comand_profile'),
]