from django.shortcuts import render
from apps.secondary import models
from apps.base.models import Settings, Instagram
# Create your views here.
def blog(request):
    insta = Instagram.objects.latest('id')
    settings = Settings.objects.latest('id')
    return render(request, 'blog.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def gallery(request):
    gallery = models.Gallery.objects.all()
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    return render(request, 'gallery.html', locals())

def grid_sidebar(request):
    return render(request, 'grid-sidebar.html', locals())

def member_login(request):
    return render(request, 'member-login.html', locals())

def my_profile(request):
    return render(request, 'my-profile.html', locals())

def quick_view(request):
    return render(request, 'quick-view.html', locals())

def single(request):
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    return render(request, 'single.html', locals())

def comand(request):
    band = models.Band.objects.all()
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    return render(request, 'comand.html', locals())