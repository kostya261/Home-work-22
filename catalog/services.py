from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные списка продуктов из кеша, если кешь пуст то из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.filter(is_published=True)
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(is_published=True)
    cache.set(key, products, timeout=60 * 15) # 15 минут
    return products


def get_products_by_category_id(category_id):
    """
    Получает опубликованные продукты по ID категории из кеша или БД
    """
    if not CACHE_ENABLED:
        return Product.objects.filter(
            category_id=category_id,
            is_published=True
        )

    # Создаем уникальный ключ для категории
    key = f"product_list_category_id_{category_id}"
    products = cache.get(key)

    if products is not None:
        return products

    # Получаем продукты с фильтрацией по ID категории
    products = Product.objects.filter(
        category_id=category_id,
        is_published=True
    ).select_related('category')  # Оптимизация запроса

    cache.set(key, products, timeout=60 * 15)  # 15 минут
    return products


def get_all_categories_from_cache():
    """
    Получает все категории из кеша или БД
    """
    if not CACHE_ENABLED:
        return Category.objects.all()

    key = "category_list"
    categories = cache.get(key)

    if categories is not None:
        return categories

    categories = Category.objects.all()
    cache.set(key, categories, timeout=60 * 15)  # 15 минут
    return categories
