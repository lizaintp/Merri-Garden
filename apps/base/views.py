from django.shortcuts import render
from apps.base import models
from apps.secondary.models import AboutNews, News

# Create your views here.
def index(request):
    news = News.objects.all().order_by('?')[:4]
    aboutnews = AboutNews.objects.latest('id')
    settings = models.Settings.objects.latest('id')
    insta = models.Instagram.objects.latest('id')
    image = models.Images.objects.latest('id')
    comments = models.Comments.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    settings = models.Settings.objects.latest('id')
    insta = models.Instagram.objects.latest('id')
    whychooseus = models.WhyChooseUs.objects.all()
    whychooseusimage = models.WhyChooseUsImage.objects.latest('id')
    about = models.About.objects.latest('id')
    aboutabout = models.AboutAbout.objects.latest('id')
    whatdoweoffer = models.WhatDoWeOffer.objects.all()
    whatdoweofferimage = models.WhatDoWeOfferImage.objects.latest('id')
    comments = models.Comments.objects.all()
    return render(request, 'base/about.html', locals())
