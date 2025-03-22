from django import template
from django.conf import settings
import os

register = template.Library()

@register.simple_tag
def media_url(image_path):
    """
    Возвращает полный URL для медиа-файла.
    Предполагает, что в базе данных хранится только имя файла,
    а не полный путь.
    """
    return os.path.join(settings.MEDIA_URL, image_path)