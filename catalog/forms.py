from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Модель для добавления продукта в базу данных"""

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

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'image']

        labels = {
            'title': 'Название товара',
            'description': 'Описание товара',
            'price': 'Цена',
            'category': 'Категория',
            'image': 'Изображение',
        }


'''
class ProductModeratorForm(forms.ModelForm):
    """Модель для добавления продукта в базу данных"""

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

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'image']

        labels = {
            'title': 'Название товара',
            'description': 'Описание товара',
            'price': 'Цена',
            'category': 'Категория',
            'image': 'Изображение',
        }'''
