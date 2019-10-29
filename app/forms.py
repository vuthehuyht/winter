from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'firstname',
        'placeholder': 'Họ'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'lastname',
        'placeholder': 'Tên'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'username',
        'placeholder': 'Userame',
        'required': 'required'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control input-lg',
        'name': 'email',
        'placeholder': 'Email',
        'required': 'required'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control input-lg',
        'name': 'password',
        'placeholder': 'Mật khẩu',
        'required': 'required'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control input-lg',
        'name': 'comfirm_password',
        'placeholder': 'Mật khẩu xác nhận',
        'required': 'required'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.get(email=email).exists():
            raise ValidationError(
                "Email đã tồn tại"
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Mật khẩu không khớp"
            )
        return password2
