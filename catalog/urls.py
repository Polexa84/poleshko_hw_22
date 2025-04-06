from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('contacts/', views.contact, name='contacts'),  # Страница контактов
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Страница с товарами
]
