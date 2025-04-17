from django.urls import path
from .views import (
    ProductListView,
    ContactView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    product_list_by_category,  # Импортируем product_list_by_category
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
    path('category/<int:category_id>/', product_list_by_category, name='product_list_by_category'), # Добавляем URL для product_list_by_category
]