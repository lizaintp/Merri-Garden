from django.shortcuts import render
from apps.secondary import models
from apps.base.models import Settings, Instagram
# Create your views here.
def blog(request):
    insta = Instagram.objects.latest('id')
    settings = Settings.objects.latest('id')
    news = models.News.objects.all()
    aboutnews = models.AboutNews.objects.latest('id')
    return render(request, 'blog.html', locals())

def gallery(request):
    gallery = models.Gallery.objects.all()
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    aboutgallery = models.AboutGallery.objects.latest('id')
    return render(request, 'gallery.html', locals())

def comand(request):
    band = models.Band.objects.all()
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    return render(request, 'comand.html', locals())

def single(request, id):
    blog = models.News.objects.get(id=id)
    settings = Settings.objects.latest('id')
    insta = Instagram.objects.latest('id')
    return render(request, 'single.html', locals())