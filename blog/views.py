from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost  # Импортируем модель BlogPost
from .forms import PostForm  # Импортируем форму PostForm
from django.urls import reverse_lazy

class BlogListView(ListView):
    """
    Представление для отображения списка постов блога.
    """
    model = BlogPost  # Используем модель BlogPost
    template_name = 'blog/blog_list.html'  # Указываем шаблон для отображения
    context_object_name = 'blog_posts'  # Имя переменной в контексте, содержащей список постов
    queryset = BlogPost.objects.filter(is_published=True).order_by('-created_at')  # Получаем только опубликованные посты, отсортированные по дате создания

class BlogDetailView(DetailView):
    """
    Представление для отображения детальной информации о посте блога.
    """
    model = BlogPost  # Используем модель BlogPost
    template_name = 'blog/blog_detail.html'  # Указываем шаблон для отображения
    context_object_name = 'blog_post'  # Имя переменной в контексте, содержащей информацию о посте

    def get_object(self, queryset=None):
        """
        Переопределение метода get_object для увеличения счетчика просмотров.
        """
        obj = super().get_object(queryset=queryset)  # Получаем объект
        obj.views_count += 1  # Увеличиваем счетчик просмотров
        obj.save()  # Сохраняем объект
        return obj  # Возвращаем объект

class BlogCreateView(CreateView):
    """
    Представление для создания нового поста блога.
    """
    model = BlogPost  # Используем модель BlogPost
    form_class = PostForm  # Используем форму PostForm
    template_name = 'blog/blog_form.html'  # Указываем шаблон для отображения
    success_url = reverse_lazy('blog:blog_list')  # URL для перенаправления после успешного создания

class BlogUpdateView(UpdateView):
    """
    Представление для редактирования поста блога.
    """
    model = BlogPost  # Используем модель BlogPost
    form_class = PostForm  # Используем форму PostForm
    template_name = 'blog/blog_form.html'  # Указываем шаблон для отображения
    context_object_name = 'blog_post'

class BlogDeleteView(DeleteView):
    """
    Представление для удаления поста блога.
    """
    model = BlogPost  # Используем модель BlogPost
    template_name = 'blog/blog_confirm_delete.html'  # Указываем шаблон для отображения
    success_url = reverse_lazy('blog:blog_list')  # URL для перенаправления после успешного удаления
    context_object_name = 'blog_post'