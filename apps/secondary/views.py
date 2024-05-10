from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html', locals())

def portfolio_page(request):
    return render(request, 'portfolio-page.html', locals())

def portfolio(request):
    return render(request, 'portfolio.html', locals())

def post(request):
    return render(request, 'post.html', locals())

def services_page(request):
    return render(request, 'services-page.html', locals())

def services(request):
    return render(request, 'services.html', locals())