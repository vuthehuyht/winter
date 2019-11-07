from django.urls import path
from . import views

product = views.ProductListView.as_view({
    'get': 'list'
})

category = views.CategoryListView.as_view({
    'get': 'list'
})

urlpatterns = [
    path('api/v1/login', views.login),
    path('api/v1/product/', product),
    path('api/v1/category/', category)
]
