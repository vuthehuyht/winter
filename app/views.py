from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'pages/blog.html')


def shop_category(request):
    return render(request, 'pages/category.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        if '@' in email:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, 'index.html')
            else:
                messages.error(request, "Tài khoản hoặc mật khẩu không đúng")
                return render(request, 'pages/login.html')
        else:
            user = authenticate(username=email, password=password)
            print(user.username)
            if user is not None:
                auth_login(request, user)
                return render(request, 'index.html')
            else:
                messages.error(request, "Tài khoản hoặc mật khẩu không đúng")
                return render(request, 'pages/login.html')
    return render(request, 'pages/login.html')
