from django.shortcuts import render

# Create your views here.
def blog_page(request):
    return render(request, 'blog-page.html', locals())

def courses(request):
    return render(request, 'courses.html', locals())

def single_blog(request):
    return render(request, 'single-blog.html', locals())

def single_course(request):
    return render(request, 'single-course.html', locals())

def teacher_profile(request):
    return render(request, 'teacher-profile.html', locals())

def teacher(request):
    return render(request, 'teacher.html', locals())