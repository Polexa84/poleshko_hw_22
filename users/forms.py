from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Имя пользователя",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9.@+-]*$',
                message="Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_.",
                code="invalid_username"
            ),
        ],
        help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_."
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Пароль"
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Подтвердите пароль"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email"
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password') # Добавили 'email' и 'password'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = get_user_model().objects.create_user(email=email, username=username, password=password)
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(  # Оставляем имя поля "username"
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Email"  # Изменяем label на "Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Пароль"
    )