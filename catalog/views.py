from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product, AddProduct


# Create your views here.

class Home(ListView):
    """ Главная страница """
    model = Product
    form_class = ProductForm()
    template_name = 'catalog/block_content.html'
    context_object_name = 'all_products'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    """ Детализация продукта """
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
    """ Контактная информация """
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class AddProductView(LoginRequiredMixin, CreateView):
    """ Добавляем продукт """
    model = Product
    form_class = AddProduct
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактируем продукт """
    model = Product
    form_class = AddProduct
    template_name = 'catalog/edit_product.html'
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        return reverse('catalog:detail_product', kwargs={'product_id': self.object.id})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление продукта """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context