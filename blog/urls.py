from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'blog'  # Имя ссылки

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),  # Просмотр списка (общедоступно)
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),  # Просмотр деталей (общедоступно)
    path('create/', login_required(views.BlogCreateView.as_view()), name='blog_create'),  # Создание (только для авторизованных)
    path('<int:pk>/update/', login_required(views.BlogUpdateView.as_view()), name='blog_update'),  # Обновление (только для авторизованных)
    path('<int:pk>/delete/', login_required(views.BlogDeleteView.as_view()), name='blog_delete'),  # Удаление (только для авторизованных)
]