from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def index(request):
    """Отображает главную страницу."""
    return render(request, 'home.html')  # Используем home.html для главной страницы

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