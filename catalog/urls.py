from django.urls import path
from .views import (
    ProductListView,
    ContactView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,  # Импортируем ProductDeleteView
)
from django.contrib.auth.decorators import login_required

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', login_required(ProductCreateView.as_view()), name='product_create'),
    path('product/<int:pk>/update/', login_required(ProductUpdateView.as_view()), name='product_update'),
    path('product/<int:pk>/delete/', login_required(ProductDeleteView.as_view()), name='product_delete'),  # Добавляем URL для удаления продукта
]