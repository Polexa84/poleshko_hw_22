from django.contrib import admin
from django.urls import path, include  # Импортируем include для подключения других urls.py

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для админ-панели Django
    path('catalog/', include('catalog.urls')),  # Подключаем URL-адреса из catalog/urls.py
]
