from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import EmailForgetPasswordForm

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('category/', views.shop_category, name='category'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='pages/password_reset_form.html',
        form_class=EmailForgetPasswordForm,
        email_template_name='pages/password_reset_email.html',
        subject_template_name='pages/password_reset_subject.html'
    ), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_confirm//<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pages/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password_reset_complete.html'
    ), name='password_reset_complete')
]
