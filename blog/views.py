from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  # Создайте этот шаблон
    context_object_name = 'blog_posts'
    queryset = BlogPost.objects.filter(is_published=True).order_by('-created_at') # Только опубликованные

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'  # Создайте этот шаблон
    context_object_name = 'blog_post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save()
        return obj

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']  # Укажите поля для формы
    template_name = 'blog/blog_form.html'  # Создайте этот шаблон
    success_url = reverse_lazy('blog:blog_list')  # URL для перенаправления после успешного создания

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']  # Укажите поля для формы
    template_name = 'blog/blog_form.html'  # Создайте этот шаблон
    context_object_name = 'blog_post'

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'  # Создайте этот шаблон
    success_url = reverse_lazy('blog:blog_list')  # URL для перенаправления после успешного удаления
    context_object_name = 'blog_post'