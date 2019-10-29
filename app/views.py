from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import requests


from .forms import (
    RegistrationForm
)


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
        url_api = 'http://127.0.0.1:8000/api/v1/login'

        if '@' in email:
            username = User.objects.get(email=email).username
            data = {'username': username,
                    'password': password}
            result = requests.post(url_api, data=data)
            if result.status_code == 404:
                messages.error(request, "Tài khoản hoặc mật khẩu không đúng")
                return render(request, 'pages/login.html')
        else:
            data = {'username': email,
                    'password': password}
            result = requests.post(url_api, data=data)
            if result.status_code == 200:
                user = authenticate(username=email, password=password)
                auth_login(request, user)
                return render(request, 'index.html')
            else:
                messages.error(request, "Tài khoản hoặc mật khẩu không đúng")
                return render(request, 'pages/login.html')
    return render(request, 'pages/login.html')


def register(request):
    form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})
