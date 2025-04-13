from django.urls import path
from .views import (
    ProductListView, ContactView, ProductDetailView,
    ProductCreateView, ProductUpdateView  # Импортируем новые представления
)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),  # URL для создания продукта
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),  # URL для редактирования продукта
]