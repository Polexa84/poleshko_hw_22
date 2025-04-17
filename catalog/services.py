from .models import Product, Category

def get_products_by_category(category_id):
    """
    Возвращает список продуктов в указанной категории.

    """
    try:
        category = Category.objects.get(pk=category_id)
        return Product.objects.filter(category=category)
    except Category.DoesNotExist:
        return Product.objects.none()  # Возвращаем пустой QuerySet, если категория не найдена