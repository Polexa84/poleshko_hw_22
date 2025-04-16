from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.backends import ModelBackend
from .forms import UserRegistrationForm, UserLoginForm
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            send_welcome_email(user.email)
            return redirect('catalog:home')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def send_welcome_email(email):
    subject = _('Добро пожаловать на наш сайт!')
    message = _('Привет, %(email)s! Спасибо за регистрацию на нашем сайте!') % {'email': email}
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('catalog:home')
            else:
                form.add_error(None, "Неверное имя пользователя или пароль")
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('catalog:home')