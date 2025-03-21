from django.contrib import admin
from django.urls import path, include  # Импортируем include для подключения других urls.py
from django.conf import settings  # Добавляем импорт settings
from django.conf.urls.static import static  # Добавляем импорт static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)