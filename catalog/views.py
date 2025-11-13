from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import Product, AddProduct

# Create your views here.
'''def home(request):
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
   
    '''


class Home(ListView):
    model = Product
    template_name = 'catalog/block_content.html'
    context_object_name = 'all_products'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_object(self):
        # Получаем статью и увеличиваем счетчик просмотров
        obj = super().get_object()

        if hasattr(obj, 'views'):
            obj.views += 1
            obj.save()
        return obj


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class AddProductView(CreateView):
    model = Product
    form_class = AddProduct
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')
