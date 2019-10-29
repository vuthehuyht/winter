from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('category/', views.shop_category, name='category'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]