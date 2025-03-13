# Skystore - Интернет-магазин (Django)

## Описание

Skystore - это учебный проект интернет-магазина, разработанный с использованием Django framework.  Основная цель проекта - изучение и практическое применение основных концепций Django, таких как:

*   Модели (Models)
*   Представления (Views)
*   Шаблоны (Templates)
*   Формы (Forms)
*   Маршрутизация URL (URL routing)
*   Работа с базами данных
*   Система аутентификации пользователей
*   Использование статических файлов (CSS, JavaScript)
*   Развертывание проекта

## Функциональность

На данный момент реализована следующая функциональность:

*   Отображение каталога товаров (в разработке).
*   Страница с контактной информацией и формой обратной связи.
*   Обработка данных формы обратной связи и отображение сообщения об успешной отправке.

В будущем планируется реализовать:

*   Полный каталог товаров с фильтрацией и сортировкой.
*   Корзину покупок.
*   Оформление заказа.
*   Личный кабинет пользователя с историей заказов.
*   Систему аутентификации и авторизации пользователей.
*   Административную панель для управления товарами и заказами.

## Технологии

*   Python 3.x
*   Django framework
*   Bootstrap (для стилизации)
*   HTML
*   CSS
*   JavaScript (по мере необходимости)
*   Git (система контроля версий)

## Установка и запуск

1.  **Клонируйте репозиторий:**

    ```bash
    git clone <ссылка_на_репозиторий>
    cd skystore
    ```

2.  **Создайте и активируйте виртуальное окружение:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate  # Windows
    ```

3.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Выполните миграции:**

    ```bash
    python manage.py migrate
    ```

5.  **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

    Перейдите по адресу `http://127.0.0.1:8000/` в вашем браузере.

## Структура проекта
