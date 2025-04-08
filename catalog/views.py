from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from .models import Product  # Импортируйте модель Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy  # Импортируем reverse_lazy для создания URL-адресов
from .forms import ProductForm

# Добавлен CBV ProductListView для главной страницы
class ProductListView(ListView):
    """
    Отображает список последних продуктов на главной странице.
    Наследуется от ListView.
    """
    model = Product  # Модель, которую используем для отображения
    template_name = 'catalog/home.html'  # Шаблон для отображения
    context_object_name = 'latest_products'  # Имя переменной в шаблоне
    queryset = Product.objects.order_by('-created_at')[:5]  # Запрос для получения данных

# Добавлен CBV ContactView для страницы контактов
class ContactView(TemplateView):
    """
    Отображает страницу контактов и обрабатывает форму обратной связи.
    Наследуется от TemplateView.
    """
    template_name = 'catalog/contacts.html'  # Шаблон для отображения

    def get_context_data(self, **kwargs):
        """
        Добавляет форму ContactForm в контекст шаблона.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()  # Передаем форму в контекст
        return context

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос при отправке формы.
        """
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Вывод сообщения об успехе
            messages.success(request, 'Сообщение успешно отправлено!')
            print("Сообщение отправлено!")

            # Перенаправление на эту же страницу, чтобы сбросить форму
            return redirect('catalog/contacts')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)

# Добавлен CBV ProductDetailView для страницы деталей продукта
class ProductDetailView(DetailView):
    """
    Отображает детальную информацию о продукте.
    Наследуется от DetailView.
    """
    model = Product  # Модель, которую используем для отображения
    template_name = 'catalog/product_detail.html'  # Шаблон для отображения
    context_object_name = 'product'  # Имя переменной в шаблоне

class ProductCreateView(CreateView):
    """
    CBV для создания нового продукта.
    Использует ProductForm для отображения полей и валидации данных.
    """
    model = Product  # Указываем модель, для которой создается объект
    form_class = ProductForm  # Указываем форму, которая будет использоваться
    template_name = 'catalog/product_form.html'  # Указываем шаблон для отображения формы создания
    success_url = reverse_lazy('catalog:home')  # Указываем URL для перенаправления после успешного создания

class ProductUpdateView(UpdateView):
    """
    CBV для обновления существующего продукта.
    Использует ProductForm для отображения полей и валидации данных.
    """
    model = Product  # Указываем модель, объект которой будет обновляться
    form_class = ProductForm  # Указываем форму, которая будет использоваться
    template_name = 'catalog/product_form.html'  # Указываем шаблон для отображения формы обновления
    success_url = reverse_lazy('catalog:home')  # Указываем URL для перенаправления после успешного обновления