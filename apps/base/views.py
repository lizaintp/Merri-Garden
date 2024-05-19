from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    insta = models.Instagram.objects.latest('id')
    image = models.Images.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    settings = models.Settings.objects.latest('id')
    insta = models.Instagram.objects.latest('id')
    whychooseus = models.WhyChooseUs.objects.all()
    about = models.About.objects.latest('id')
    whatdoweoffer = models.WhatDoWeOffer.objects.all()
    comments = models.Comments.objects.all()
    return render(request, 'base/about.html', locals())
