from django.shortcuts import render
from apps.base.models import Instagram, Settings
from apps.secondary.models import AboutGallery
from apps.contacts import models

# Create your views here.
def contact(request):
    aboutgallery = AboutGallery.objects.latest('id')
    insta = Instagram.objects.latest('id')
    settings = Settings.objects.latest('id')
    quetions = models.Quetions.objects.all()
    aboutcontacts = models.AboutContacts.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        result = models.Contacts.objects.create(name = name, email = email, subject = subject, message=message)
    return render(request, 'base/contact.html', locals())