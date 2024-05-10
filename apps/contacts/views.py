from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'base/contact.html', locals())