from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from .models import Product  # Импортируйте модель Product


def index(request):
    """Отображает главную страницу."""
    latest_products = Product.objects.order_by('-created_at')[:5]
    context = {'latest_products': latest_products}
    return render(request, 'home.html', context)

def contact(request):
    """Отображает страницу с контактной информацией и формой обратной связи."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Вывод сообщения об успехе
            messages.success(request, 'Сообщение успешно отправлено!')
            print("Сообщение отправлено!")  # Добавляем отладочный вывод

            # Перенаправление на эту же страницу, чтобы сбросить форму
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})


def product_detail(request, pk):
    """Отображает страницу с подробной информацией о продукте."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})