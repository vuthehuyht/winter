import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token

from .forms import (
    RegistrationForm
)


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'pages/blog.html')


def shop_category(request):
    url_api = 'http://127.0.0.1:8000/api/v1/product'
    token, _ = Token.objects.get_or_create(user=request.user)
    headers = {'Authorization': 'Token ' + token.key}
    result = requests.get(url_api, headers=headers)
    args = {}
    args.update(csrf(request))
    args['contents'] = result.json()
    return render(request, 'pages/category.html', args)


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
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'pages/register.html', {'form': form})
    form = RegistrationForm()
    return render(request, 'pages/register.html', {'form': form})
