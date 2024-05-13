from django.urls import path
from apps.secondary.views import blog_page, courses, single_blog, single_course, teacher, teacher_profile

urlpatterns = [
    path('blog_page', blog_page, name = 'blog_page'),
    path('courses', courses, name = 'courses'),
    path('single_blog', single_blog, name = 'single_blog'),
    path('single_course', single_course, name = 'single_course'),
    path('teacher', teacher, name = 'teacher'),
    path('teacher-profile', teacher_profile, name = 'teacher-profile'),
]