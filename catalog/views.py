from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .services import get_products_by_category
from django.core.cache import cache


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'latest_products'

    def get_queryset(self):
        cache_key = 'latest_products'
        latest_products = cache.get(cache_key)

        if latest_products is None:
            latest_products = Product.objects.order_by('-created_at')[:5]
            cache.set(cache_key, latest_products, 60 * 15)  # Кэшируем на 15 минут

        return latest_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        user = self.request.user
        context['can_add_product'] = user.has_perm('catalog.add_product')
        return context


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Сообщение успешно отправлено!')
            print("Сообщение отправлено!")
            return redirect('catalog:contacts')  # Исправлено на правильный URL
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['can_unpublish'] = user.has_perm('catalog.can_unpublish_product')
        context['can_delete'] = user.has_perm('catalog.delete_product')
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        context = {
            'form': form,
            'categories': Category.objects.all(),
        }
        return render(self.request, self.template_name, context)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.can_unpublish_product'

    def form_invalid(self, form):
        print(form.errors)
        context = {
            'form': form,
            'categories': Category.objects.all(),
        }


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


def product_list_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    cache_key = f'products_by_category_{category_id}'
    products = cache.get(cache_key)

    if products is None:
        products = get_products_by_category(category_id)
        cache.set(cache_key, products, 60 * 15)

    context = {
        'category': category,
        'products': products,
        'categories': Category.objects.all(),
    }

    return render(request, 'catalog/product_list_by_category.html', context)