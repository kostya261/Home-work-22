import os

from django.core.exceptions import ValidationError
from django.db import models
from django import forms


# Create your models here.

def validate_image_size(value):
    """ валидатор """
    """ Проверка размера файла """
    filesize = value.size
    if filesize > 5242880:
        raise ValidationError("Максимальный размер файла 5Мб.")


def validate_image_extension(value):
    """ валидатор """
    """ Проверка расширения файла """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Поддерживаются только файлы JPEG и PNG!')


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
    image = models.ImageField(
        upload_to='photos/',
        verbose_name='Фотография',
        blank=True,
        null=True,
        validators=[validate_image_size, validate_image_extension]
    )
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

    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'title':
                field.widget.attrs['placeholder'] = 'Введите название товара'
            elif field_name == 'description':
                field.widget.attrs['placeholder'] = 'Подробное описание товара'
                field.widget.attrs['rows'] = '4'
            elif field_name == 'price':
                field.widget.attrs['placeholder'] = 'Цена в рублях'
                field.widget.attrs['min'] = '0'
            elif field_name == 'image':
                field.widget.attrs['class'] = 'form-control-file'  # особый класс для файлов

    def clean_title(self):
        """Валидация названия товара"""
        title = self.cleaned_data['title']
        title_lower = title.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in title_lower:
                raise ValidationError(f'Название содержит запрещенное слово: "{word}"')

        return title

    def clean_description(self):
        """ Валидация описания товара """
        description = self.cleaned_data['description']
        description_lower = description.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in description_lower:
                raise ValidationError(f'Описание содержит запрещенное слово: "{word}"')

        return description

    def clean_price(self):
        """ Валидация цены """
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError("Цена не должна быть отрицательной!")
        return price

    def clean_image(self):
        """ Валидация изображения """
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5242880:
                raise forms.ValidationError('Размер изображения больше 5Мб.!')

            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                raise forms.ValidationError('только JPEG или PNG формат файлов!')

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'image', 'is_published']

        labels = {
            'title': 'Название товара',
            'description': 'Описание',
            'price': 'Цена (руб)',
            'category': 'Категория',
            'image': 'Изображение',
        }
