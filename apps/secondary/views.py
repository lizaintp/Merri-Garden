from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html', locals())

def courses(request):
    return render(request, 'courses.html', locals())

def single_blog(request):
    return render(request, 'single-blog.html', locals())

def single_course(request):
    return render(request, 'single-course.html', locals())

def comand_profile(request):
    return render(request, 'comand-profile.html', locals())

def comand(request):
    return render(request, 'comand.html', locals())