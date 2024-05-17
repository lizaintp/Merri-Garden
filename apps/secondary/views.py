from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html', locals())

def blog_sidebar(request):
    return render(request, 'blog-sidebar.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def checkout(request):
    return render(request, 'checkout.html', locals())

def cart(request):
    return render(request, 'cart.html', locals())

def checkout(request):
    return render(request, 'checkout.html', locals())

def grid_sidebar(request):
    return render(request, 'grid-sidebar.html', locals())

def member_login(request):
    return render(request, 'member-login.html', locals())

def my_profile(request):
    return render(request, 'my-profile.html', locals())

def quick_view(request):
    return render(request, 'quick-view.html', locals())

def single(request):
    return render(request, 'single.html', locals())

def vendor_shop(request):
    return render(request, 'vendor-shop.html', locals())