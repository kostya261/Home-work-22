from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import ProductForm
from .models import Product, AddProduct


# Create your views here.

class Home(ListView):
    model = Product
    form_class = ProductForm()
    template_name = 'catalog/block_content.html'
    context_object_name = 'all_products'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    form_class = ProductForm()
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
    success_url = reverse_lazy('catalog:home')
