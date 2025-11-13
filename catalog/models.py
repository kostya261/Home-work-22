from django.db import models
from django import forms


# Create your models here.


class Category(models.Model):
    """ Описание Категории товаров """
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description or ''

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """ Описание продукта """
    title = models.CharField(max_length=100, verbose_name='наименование', unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='категория')
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.description or ''

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['title', ]


class AddProduct(forms.ModelForm):
    """Модель для добавления продукта в базу данных"""

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Название товара',
            'description': 'Описание',
            'price': 'Цена (руб)',
            'category': 'Категория',
            'image': 'Изображение',
        }
