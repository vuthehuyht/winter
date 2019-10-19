from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'pages/blog.html')


def shop_category(request):
    return render(request, 'pages/category.html')
