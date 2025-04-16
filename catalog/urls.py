from django.urls import path
from .views import (
    ProductListView, ContactView, ProductDetailView,
    ProductCreateView, ProductUpdateView  # Импортируем новые представления
)
from django.contrib.auth.decorators import login_required  # Импортируем login_required

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),  # Список товаров (общедоступный)
    path('contacts/', ContactView.as_view(), name='contacts'),  # контакты (общедоступный)
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'), # Детали продукта (общедоступный)
    path('product/create/', login_required(ProductCreateView.as_view()), name='product_create'),  # Создание продукта (защищено)
    path('product/<int:pk>/update/', login_required(ProductUpdateView.as_view()), name='product_update'),  # Редактирование продукта (защищено)
]