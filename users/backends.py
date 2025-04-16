from django.contrib.auth.backends import ModelBackend
from .models import User

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Ищем пользователя по email
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)  # Получение пользователя по ID
        except User.DoesNotExist:
            return None