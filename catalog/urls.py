from django.urls import path
from .views import ProductListView, ContactView, ProductDetailView  # Импортируем CBV

# Обновлены URL для использования CBV
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),  # Главная страница (CBV)
    path('contacts/', ContactView.as_view(), name='contacts'),  # Страница контактов (CBV)
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Страница с товарами (CBV)
]