from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email Address')  # Уникальный email
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')  # Аватар пользователя
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone Number')  # Номер телефона
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Country')  # Страна

    USERNAME_FIELD = 'email'  # Используем email для авторизации
    REQUIRED_FIELDS = ['username']  # username все еще обязателен

    def __str__(self):
        return self.email