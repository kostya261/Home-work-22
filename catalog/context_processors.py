from django.core.cache import cache
from catalog.models import Category
from config.settings import CACHE_ENABLED


def categories(request):
    """Добавляет все категории в контекст всех шаблонов"""
    if not CACHE_ENABLED:
        categories_list = Category.objects.all()
    else:
        key = "all_categories"
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list, timeout=60 * 60)  # 1 час

    return {
        'all_categories': categories_list
    }
