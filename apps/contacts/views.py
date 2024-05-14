from django.shortcuts import render
from apps.contacts import models

# Create your views here.
def contact(request):
    contact = models.Contacts.objects.all()
    return render(request, 'base/contact.html', locals())