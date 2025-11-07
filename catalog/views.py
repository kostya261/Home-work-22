from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Product, AddProduct


# Create your views here.
def home(request):
    """Коннектор для отображения страницы home.html"""

    all_products = Product.objects.all()  # .order_by('-created_at', '-id')[:5]
    context = {
        'all_products': all_products
    }

    return render(request, 'catalog/block_content.html', context)


def detail_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }

    return render(request, 'catalog/product_detail.html', context)


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


def add_product(request):
    """ Коннектор для добавления продукта в базу данных"""
    if request.method == 'POST':

        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            # Сохраняем товар в базу
            form.save()
            # Перенаправляем на главную или страницу если всё хорошо
            return redirect('/')

    else:

        form = AddProduct()

    context = {'form': form}
    return render(request, 'catalog/add_product.html', context)
