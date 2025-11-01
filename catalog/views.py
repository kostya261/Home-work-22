from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


# Create your views here.
def home(request):
    """Коннектор для отображения страницы home.html"""

    """ Получаем последние 5 созданных продуктов """
    latest_products = Product.objects.all().order_by('-created_at', '-id')[:5]

    context = {
        'latest_products': latest_products
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    """Коннектор для отображения страницы contacts.html и обработки POST запроса"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')
