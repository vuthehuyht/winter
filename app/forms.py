from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'firstname',
        'placeholder': 'Họ',
        'autofocus': 'autofocus'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'lastname',
        'placeholder': 'Tên'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control input-lg',
        'name': 'username',
        'placeholder': 'Username',
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                "Tên tài khoản trên đã tồn tại"
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Email trên đã tồn tại"
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


class EmailForgetPasswordForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "Không tìm thấy địa chỉ email"
            )
        return email
